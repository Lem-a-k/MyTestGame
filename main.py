from test import is_prime

if __name__ == '__main__':
    tests = [(2, True, ''),
             (4, False, ''),
             (7, True, ''),
             (9, False, ''),
             (12, False, '')]
    excepts = [(1, Exception), (0, Exception), (-1, Exception)]
    flag = True
    try:
        for test, res, comment in tests:
            assert is_prime(test) == res, comment
    except AssertionError as e:
        flag = False
    except Exception:
        flag = False
    for test, ex in excepts:
        try:
            is_prime(test)
        except ex:
            pass
        except Exception:
            flag = False
        else:
            flag = False
    print('YES' if flag else 'NO')
