'''
8)

a) Write a function called print_arguments with one parameter named function.
The function will return one new function which prints the
arguments and the keyword arguments received and will return
the output of the function receives as a parameter.
Example:
def multiply_by_two(x):
    return x * 2

def add_numbers(a, b):
    return a + b

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)  # this will print:
Arguments are: (10,), {} and will return 20.

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)  # this will print:
Arguments are: (3, 4), {} and will return 7.
'''

def print_arguments(function):
    def newfunc(*args,**kwargs):
        print(args,kwargs)
        return function(*args,**kwargs)
    return newfunc

def suma(a,b,c):
    return a+b+c

augmented = print_arguments(suma)
print(augmented(10,20,30))


'''
b) Write a function called multiply_output with 
one parameter named function. The function will 
return one new function which returns the output 
of the function received multiplied by 2.
Example:

def multiply_by_three(x):
    return x * 3

augmented_multiply_by_three = multiply_output(multiply_by_three)
x = augmented_multiply_by_three(10)  # this will return 2 * (10 * 3)

'''

def multiply_output(function):
    def newfunc(*args,**kwargs):
        return function(*args,**kwargs)*2
    return newfunc

example  = multiply_output(suma)
print(example(10,20,30))