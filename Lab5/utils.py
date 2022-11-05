'''
1)
a) Write a module named utils.py that contains one function called process_item.
The function will have one parameter, x, and will return the least prime number
greater than x. When run, the module will request an input from the user,
convert it to a number and it will display the output of the process_item function.
'''

def process_item(x):
    import sympy.ntheory as nt
    try:
        x = int(x)
    except:
        print("Input not valid. Insert a number!")
        return
    x_cpy = x+1
    while not nt.isprime(x_cpy):
        x_cpy += 1
    return x_cpy
