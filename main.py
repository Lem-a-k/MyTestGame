from yandex_testing_lesson import is_palindrome

if __name__ == '__main__':
    tests = [('', True, 'empty string'),
             ('a', True, ''),
             ('aba', True, ''),
             ('abc', False, 'not palindrome'),
             ('ab', False, ''),
             ('abccba', True, ''),
             ('abcbca', False, 'wrong order')]
    try:
        for test, res, comment in tests:
            assert is_palindrome(test) == res, comment
    except AssertionError as e:
        print('NO')
        # print(e)
    else:
        print('YES')
