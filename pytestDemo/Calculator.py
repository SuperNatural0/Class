class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except TypeError as Exception:
            return '这两个数必须都为数字类型'
            print(Exception)

    def deduct(self, a, b):
        try:
            return a - b
        except TypeError as Exception:
            return '这两个数必须都为数字类型'
            print(Exception)

    def multiply(self, a, b):
        try:
            return (float('%.2f' % (a * b)))
        except TypeError as Exception:
            return '这两个数必须都为数字类型'
            print(Exception)

    def divide(self, a, b):
        try:
            return (float('%.2f' % (a / b)))
        except ZeroDivisionError as Exception1:
            return "被除数不应为0"
            print(Exception)
        except TypeError as Exception2:
            return "这两个数必须都为数字类型"
            print(Exception2)


print(Calculator().divide(-1.3, 2.6))
print(Calculator().add('20.0000000004', 2))
print(Calculator().multiply(-1.3, -3.9))
