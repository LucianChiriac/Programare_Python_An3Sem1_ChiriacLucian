'''
 Using functions, anonymous functions, list comprehensions and filter,
implement three methods to generate a list with all the vowels in a given string.

For the string "Programming in Python is fun"
the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].


'''

def get_vowels(text):
    rez = []
    for letter in text:
        if letter in ['a','e','i','o','u']:
            rez.append(letter)
    return rez

lbd_vowels = lambda text: [x for x in text if x in ['a','e','i','o','u']]

text = "Programming in Python is fun"
l_comp = list(filter(lambda x: x in ['a','e','i','o','u'],text))

print(get_vowels("Programming in Python is fun"))
print(lbd_vowels("Programming in Python is fun"))
print(l_comp)