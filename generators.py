# generators 


def square(n):
    for i in range(n):
        yield i**2


for i in square(3):
    print(i)