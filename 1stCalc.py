

def func_x():
    print "Hello World"


def func_y(x):
    return 1



def test_func():
    assert func_y(3) == 2


if __name__ == "__main__":
    func_x()
    func_y(666)
    test_func()
else:
    func_y(6)
