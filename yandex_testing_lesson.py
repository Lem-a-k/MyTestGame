def is_prime(x):
    if x < 2:
        raise Exception
    return x % 2 != 0 or x == 2
