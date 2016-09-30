# decorators are used to modifying the functionality of the function without
# touching the code of it. It is very useful when you need to extend the
# functionality.

# decorator function
def decor(func):
    # wrapper function
    def wrap():
        print('*****************')
        func()
        print('******************')
    return wrap

def hello():
    print("  Hello World!!")

# calling the decor function manually
decorhello = decor(hello)
decorhello()
# out put:
# *****************
#   Hello World!!
# ******************

# python provides simpler way to call it

@decor
def howare():
    print("  How are you")

howare()

