import pytest

# 该文件名不能更改
from Calculator import Calculator


@pytest.fixture
def connectDb():
    # 相当于setup
    print("连接数据库")
    yield "搜索结果"  # 返回后面的结果，yield相当于return
    # 相当于 teardown操作
    print("断开连接")


@pytest.fixture(scope="class")
def initcalc_class():
    # setup
    print("开始")
    calc = Calculator()
    yield calc  # return 记录上一次的执行结果，下次调用的时候直接执行后面的动作
    # teardown
    print("结束")


@pytest.fixture(params=[[1, 2, 0.5], [1, 0, '被除数不应为0'], [0, -1, 0], [0, 0, '被除数不应为0'], [-1.3, 3.9, -0.33], [-4, -2, 2],
                        [5, -4, -1.25],
                        [0.3, 0.3, 1],
                        ['123', 1, '这两个数必须都为数字类型'], [123, '1', '这两个数必须都为数字类型'], [True, 1, 1], [False, 1, 0],
                        [True, False, '被除数不应为0'], ])
def getData(request):
    return request.param


def test_getData(getData):
    print(getData)
