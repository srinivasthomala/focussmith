"""Keys made after the FocusSmith rename start with fs_; older ff_ keys keep working."""

from app.auth import generate_api_key, hash_api_key
from app.db_models import ApiKey


def test_new_keys_start_with_fs():
    raw, key_hash, prefix = generate_api_key()
    assert raw.startswith("fs_")
    assert prefix.startswith("fs_")
    assert key_hash == hash_api_key(raw)


def _add_key(db, raw, user="key-owner"):
    db.add(ApiKey(user_id=user, key_hash=hash_api_key(raw), prefix=raw[:11], label="test"))
    db.commit()


def test_legacy_ff_key_still_authenticates(anon_client, db_session):
    _add_key(db_session, "ff_legacy-key-made-before-rename")
    r = anon_client.get("/settings", headers={"Authorization": "Bearer ff_legacy-key-made-before-rename"})
    assert r.status_code == 200


def test_new_fs_key_authenticates(anon_client, db_session):
    raw, _, _ = generate_api_key()
    _add_key(db_session, raw)
    r = anon_client.get("/settings", headers={"Authorization": f"Bearer {raw}"})
    assert r.status_code == 200


def test_unknown_key_is_rejected(anon_client):
    r = anon_client.get("/settings", headers={"Authorization": "Bearer fs_not-a-real-key"})
    assert r.status_code == 401


def test_extension_keys_cannot_delete_the_account(anon_client, db_session):
    for raw in ("fs_new-style-key", "ff_old-style-key"):
        _add_key(db_session, raw)
        r = anon_client.delete("/account", headers={"Authorization": f"Bearer {raw}"})
        assert r.status_code == 401
