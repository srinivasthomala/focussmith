"""/me: the dashboard records the account email from its verified token; the
extension reads it back with its key."""

import pytest
from fastapi.testclient import TestClient

from app.auth import get_current_user, get_current_web_claims
from app.database import get_db
from app.db_models import UserSettings
from app.main import app
from tests.conftest import TEST_USER


@pytest.fixture
def make_client(db_session):
    def build(claims):
        def override_get_db():
            yield db_session

        app.dependency_overrides[get_db] = override_get_db
        app.dependency_overrides[get_current_user] = lambda: TEST_USER
        app.dependency_overrides[get_current_web_claims] = lambda: claims
        return TestClient(app)

    yield build
    app.dependency_overrides.clear()


def test_email_is_unknown_until_the_dashboard_syncs(make_client):
    client = make_client({"sub": TEST_USER, "email": "me@example.com"})
    assert client.get("/me").json() == {"email": None}


def test_sync_stores_the_token_email_and_keeps_settings(make_client, db_session):
    db_session.add(UserSettings(user_id=TEST_USER, blocklist='["reddit.com"]', blocking_mode="always"))
    db_session.commit()
    client = make_client({"sub": TEST_USER, "email": "me@example.com"})

    assert client.post("/me/sync").json() == {"email": "me@example.com"}
    assert client.get("/me").json() == {"email": "me@example.com"}
    row = db_session.get(UserSettings, TEST_USER)
    assert row.blocklist == '["reddit.com"]' and row.blocking_mode == "always"


def test_sync_creates_a_default_row_for_new_users(make_client, db_session):
    client = make_client({"sub": TEST_USER, "email": "new@example.com"})
    client.post("/me/sync")
    row = db_session.get(UserSettings, TEST_USER)
    assert row.email == "new@example.com" and row.blocklist == "[]" and row.blocking_mode == "focus-only"


def test_body_cannot_set_the_email(make_client):
    client = make_client({"sub": TEST_USER, "email": "real@example.com"})
    client.post("/me/sync", json={"email": "someone-else@example.com"})
    assert client.get("/me").json() == {"email": "real@example.com"}


def test_extension_key_cannot_sync(anon_client):
    r = anon_client.post("/me/sync", headers={"Authorization": "Bearer fs_some-extension-key"})
    assert r.status_code == 401
