

# Write a function that takes an unknown number of arguments and returns their sum.
def sum_numbers(*args):
    return sum(args)

result = sum_numbers(13, 45, 21, 17)
print(result)  



# Write a function that takes two arguments, the first being a string and the second being an unknown number of integers.
# The function should return a new string where the integers have been added to the original string

def add_numbers_to_string(string, *args):
    total = sum(args)
    return f"{string} {total}"

result = add_numbers_to_string("The total is:", 8, 9, 10)
print(result)  

# Write a function that takes an unknown number of keyword arguments and returns a dictionary
# where the keys are the argument names and the values are the argument values.

def create_dictionary(**kwargs):
    return kwargs

result = create_dictionary(name="Ruth", age=18, city="Kisumu")
print(result)  


# Write a function that takes a function and an unknown number of arguments,
# and returns the result of calling the function with the arguments.

def call_function(func, *args):
    return func(*args)

def add_numbers(x, y):
    return x + y

result = call_function(add_numbers, 2, 3)
print(result)  


# Write a function that takes a list of integers and an unknown number of keyword arguments. 
# The function should return a new list where each integer
# in the original list has been multiplied by the value of the corresponding keyword argument.


def multiply_numbers(numbers, **kwargs):
    result = []
    for i, number in enumerate(numbers):
        if i < len(kwargs):
            result.append(number * kwargs[f"arg{i+1}"])
        else:
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers, arg1=2, arg2=3)
print(result)  
  


# Write a function that takes a list of integers and
# an unknown number of additional integers as arguments. The function should 
# return the index of the first occurrence of the sum of the list and the additional integers
def find_sum_index(numbers, *args):
    total = sum(numbers) + sum(args)
    return numbers.index(total)

numbers = [1, 2, 3, 4, 5]
result = find_sum_index(numbers, 6, 7)
print(result)  


# Write a function that takes an unknown number of keyword arguments, each with a string value.
#  The function should concatenate all the strings and return the resulting string.

def concatenate_strings(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += value
    return result

result = concatenate_strings(first="Hi", second="Ruth", third="!")
print(result)  






