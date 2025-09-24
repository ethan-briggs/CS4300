import task7

def test_status_code(monkeypatch):
    class DummyResponse: status_code = 200
    monkeypatch.setattr("requests.get", lambda *a, **k: DummyResponse())
    assert task7.get_status_code() == 200
