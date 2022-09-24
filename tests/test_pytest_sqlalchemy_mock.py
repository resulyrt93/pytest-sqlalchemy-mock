from .data import MockData


def test_get_session(session):
    assert session.execute("SELECT 5").scalar() == 5


def test_session_user_table(session):
    assert session.execute("SELECT count(*) from user").scalar() == 0


def test_mocked_session_user_table(mocked_session):
    user_data = mocked_session.execute("SELECT * from user;").first()
    raw_data = MockData.USER_DATA[0]
    assert user_data[0] == raw_data["id"]
    assert user_data[1] == raw_data["name"]
    assert user_data[2] == raw_data["surname"]
    assert user_data[3] == raw_data["is_admin"]
    assert user_data[4] == raw_data["city"]
