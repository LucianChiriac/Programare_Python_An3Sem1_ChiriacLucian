'''
Write a function that receives a list with integers as parameter
that contains an equal number of even and odd numbers
that are in no specific order.
The function should return a list of pairs (tuples of 2 elements)
of numbers (Xi, Yi) such that Xi is the i-th even number
in the list and Yi is the i-th odd number

Example:
my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]

'''

def my_function(lista):
    even = [e for e in lista if e%2 == 0]
    odd = [e for e in lista if e%2 == 1]
    rez = []
    if (len(odd) != len(even)):
        print("Invalid dataset: you must have the same number of odd and even numbers")
    for i in range(0,len(odd)):
        rez.append((even[i],odd[i]))
    return rez
my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2])
