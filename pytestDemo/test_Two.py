# conftest里有对应的fixture   同级的conftest里没有就找父级的
def test_c(connectDb):
    print(connectDb)
    print("hhhhhhh")
