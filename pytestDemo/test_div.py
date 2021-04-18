import pytest


# 参数化功能用fixture实现
class TestDiv:

    def test_Divide(self, initcalc_class, getData):
        assert getData[2] == initcalc_class.divide(getData[0], getData[1])
