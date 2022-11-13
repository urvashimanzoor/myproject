def my_decorator(func):
    def wrap_func():
        print('++++++++++++++++++++++++')
        func()
        print('#########################')
    return wrap_func()
@my_decorator
def hello():
    print("hello")

@my_decorator
def bye():
    print("see ya")

#hello2= my_decorator(hello)
# second= my_decorator(bye)
# the above line is actually what @new_decorator is doing
#print(hello2)
# print(second)
hello
bye

#@my_decorator is doing here that it is taking hello as argument for my_dec fn

