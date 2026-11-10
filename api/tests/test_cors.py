"""The extension calls the API without a host permission, so CORS must allow
extension origins (and nothing else unexpected)."""

EXT = "chrome-extension://kdmocfjodfgaadcbfbmhmehkhdepaiej"


def _preflight(client, origin):
    return client.options(
        "/settings",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "authorization",
        },
    )


def test_extension_origin_is_allowed(client):
    r = _preflight(client, EXT)
    assert r.status_code == 200
    assert r.headers["access-control-allow-origin"] == EXT
    r = client.get("/settings", headers={"Origin": EXT})
    assert r.headers["access-control-allow-origin"] == EXT


def test_other_origins_are_not_allowed(client):
    for origin in ("https://evil.example", "chrome-extension://not-a-real-id", "moz-extension://abc"):
        r = _preflight(client, origin)
        assert "access-control-allow-origin" not in r.headers
