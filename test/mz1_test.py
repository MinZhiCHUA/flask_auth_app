from project.models import add_func


# def add_func (a,b):
#     return a + b


def test_add_func():
    assert add_func(1,5) == 6

