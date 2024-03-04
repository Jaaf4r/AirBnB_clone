def my_function(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_function(1, 2, 3, name='Alice', age=30, city='New York')
# Output: Positional arguments:
#           1
#           2
#           3
#
#         Keyword arguments:
#           name: Alice
#           age: 30
#           city: New York
