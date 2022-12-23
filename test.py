def is_prime(n):
    if n < 2:
        raise ValueError
    for divisor in range(2, round(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        print('YES' if is_prime(int(input())) else 'NO')
    except ValueError:
        print('NO')
