'''
 Write a function that receives a variable number of arguments and keyword arguments.
The function returns a list containing only the arguments which are dictionaries,
 containing minimum 2 keys and at least one string key with minimum 3 characters.
Example:

my_function(
 {1: 2, 3: 4, 5: 6},
 {'a': 5, 'b': 7, 'c': 'e'},
 {2: 3},
 [1, 2, 3],
 {'abc': 4, 'def': 5},=
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}
) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]
'''


def my_function(*args, **kwargs):
    rez = []
    args = [x for x in args if type(x) is dict]
    args+= [y for y in kwargs.values() if type(y) is dict]
    args = [x for x in args if len(x.keys())>=2]
    for arg in args:
        for key in arg.keys():
            if type(key) is str and len(key)>=3:
                rez += [arg]
                break
    return rez
#%%
my_function({1: 2, 3: 4, 5: 6},{'a': 5, 'b': 7, 'c': 'e'},{2: 3},[1, 2, 3], {'abc': 4, 'def': 5},3764, dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},test={1: 1, 'test': True})