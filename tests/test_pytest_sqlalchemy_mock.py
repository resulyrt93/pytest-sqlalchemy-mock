def test_get_session(session):
    assert session.execute("SELECT 5").scalar() == 5
