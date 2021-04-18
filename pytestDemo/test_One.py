# content of test_sample.py
import pytest


def inc(x):
    return x + 1


@pytest.mark.ase
def test_answer():
    assert inc(4) == 5


@pytest.fixture()
def login():
    print("login")
    username = 'zhj'
    return username


class TestAB:
    def test_a(self, login):
        print(f"hello username = {login}")

    def test_b(self):
        print("python")

    # 入口函数


if __name__ == '__main__':
    pytest.main(['test_One.py::TestAB', '-v'])
