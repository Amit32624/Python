def arithmetic_mean(x, *l):
    """ The function calculates the arithmetic mean of a non-empty
        arbitrary number of numbers """
    tot = x
    for i in l:
        tot = tot + i

    return tot / (1.0 + len(l))



print(arithmetic_mean(4,7,9))
