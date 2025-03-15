# iterator 

iterator=iter([1,2,3,4,5])
print(type(iterator))



# how to iterate

print(next(iterator))
print(next(iterator))

try:
    print(next(iterator))
except StopIteration:
    print("There are no elements in the iterator")


my_string = "Hello"
string_iterator = iter(my_string)

print(next(string_iterator))  # Output: H
print(next(string_iterator))  # Output: e