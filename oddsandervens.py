def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)


def is_odd(y):
    return not is_even(y)

#654321
print(is_even(81))
print(is_odd(7))