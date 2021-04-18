import pytest


@pytest.fixture(params=[["tom", 123], ["jerry", 456], ["linda", 789]], ids=["tom", "jerry", "linda"])
def login(request):
    print(request.param)


# print("login")


def test_login(login):
    print(login)
