from hamcrest import assert_that, is_


def test_True_is_True():
    assert_that(True, is_(True))
