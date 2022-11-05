'''
2) Create a function and an anonymous function that receive a
variable number of arguments. Both will return the sum of the
values of the keyword arguments.

Example:
For the call my_function(1, 2, c=3, d=4) the returned value will be 7.
'''

def my_function(*p,**kwargs):
    sum=0
    for key,value in kwargs.items():
        sum += value
    return sum

anonymus = lambda *arg,**kwargs : sum(kwargs.values())

print(my_function(1,2,c=3,d=4))
print(anonymus(1,2,c=3,d=4))
#%%
