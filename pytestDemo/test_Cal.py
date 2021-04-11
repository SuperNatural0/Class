import pytest

from Calculator import Calculator


class Test_cal:

    def setup_class(self):  # 类的级别，只调用一次
        self.cal = Calculator()
        print("开始")

    def teardown_class(self):
        print("结束")

    @pytest.mark.parametrize("a, b, expect", [
        [1, 2, 3], [0, 1, 1], [0, -1, -1], [0, 0, 0], [1, 9, 10], [-1, 2, 1], [999, -999, 0], [9.9, 0.1, 10],
        ['123', 1, '这两个数必须都为数字类型'], [123, '1', '这两个数必须都为数字类型'], [True, 1, 2], [False, 1, 1], [True, False, 1]
    ])
    def test_Add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [1, 2, -1], [1, 0, 1], [0, -1, 1], [0, 0, 0], [-1.3, 3, -4.3], [9.9, 0.9, 9], [5, -4, 9], [9, -2.5, 11.5],
        ['123', 1, '这两个数必须都为数字类型'], [123, '1', '这两个数必须都为数字类型'], [True, 1, 0], [False, 1, -1], [True, False, 1]
    ])
    def test_Deduct(self, a, b, expect):
        assert expect == self.cal.deduct(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [1, 2, 2], [1, 0, 0], [0, -1, 0], [0, 0, 0], [-1.3, 3, -3.9], [-1, -2, 2], [5, -4, -20], [0.3, 0.3, 0.09],
        [-4.5, -2.1, 9.45],
        ['123', 1, '这两个数必须都为数字类型'], [123, '1', '这两个数必须都为数字类型'], [True, 1, 1], [False, 1, 0], [True, False, 0]
    ])
    def test_Multiply(self, a, b, expect):
        print(self.cal.multiply(a, b))
        assert expect == self.cal.multiply(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [1, 2, 0.5], [1, 0, '被除数不应为0'], [0, -1, 0], [0, 0, '被除数不应为0'], [-1.3, 3.9, -0.33], [-4, -2, 2], [5, -4, -1.25],
        [0.3, 0.3, 1],
        ['123', 1, '这两个数必须都为数字类型'], [123, '1', '这两个数必须都为数字类型'], [True, 1, 1], [False, 1, 0], [True, False, '被除数不应为0']
    ])
    def test_Divide(self, a, b, expect):
        assert expect == self.cal.divide(a, b)
