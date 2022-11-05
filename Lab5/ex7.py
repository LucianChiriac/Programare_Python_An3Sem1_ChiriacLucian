'''

def sum_digits(x):
    return sum(map(int, str(x)))

process(
    filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
    limit=2,
    offset=2
) returns [34, 144]

Explanation:
# Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
# Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
# After offset: 34, 144, 610, 2584, 10946, 832040
# After limit: 34, 144
'''

def process(**kwargs):
    fibonnaci = [0,1]
    for i in range(0,998):
        fibonnaci.append(fibonnaci[-1]+fibonnaci[-2])
    if "filters" in kwargs.keys():
        for flt in kwargs["filters"]:
            fibonnaci = list(filter(flt,fibonnaci))
    if "offset" in kwargs.keys() and type(kwargs["offset"]) == int:
        fibonnaci = fibonnaci[kwargs["offset"]:]
    if "limit" in kwargs.keys() and type(kwargs["limit"]) == int:
        fibonnaci = fibonnaci[:kwargs["limit"]]
    return fibonnaci


def sum_digits(x):
    return sum(map(int, str(x)))


process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],limit=2,offset=2)