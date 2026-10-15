from app import app


def test_home_page_returns_app_title():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"My DevOps Portfolio App" in response.data


def test_health_endpoint_returns_ok_status():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}