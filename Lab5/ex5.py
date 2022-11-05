'''
) Write a function with one parameter which represents a list.
The function will return a new list containing all the numbers found in the given list.
Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]


'''
rezultat = []

def my_function(lista):
    rez = []
    for element in lista:
        if (str(type(element)).split("'")[1] in ['float','int','long']):
            rez.append(element)
    return rez
my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0])