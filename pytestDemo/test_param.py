# 参数化
import pytest


@pytest.mark.parametrize("key, result", [
    ['docker', 200], ['selenium', 404], ['portainer', 500],
], ids=['a', 'b', 'c'])
def test_interface(key, result):
    url = f"http://ceshiren.com/key={key}"
    print(url, result)
