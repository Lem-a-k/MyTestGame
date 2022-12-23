from yandex_testing_lesson import strip_punctuation_ru


def good_strip_punct(line):
    text = ''.join(x for x in line if x.isalpha() or x.isspace()
                   or x == '-').replace(' - ', ' ')
    return ' '.join(text.split())


if __name__ == '__main__':
    tests = ["Мама мыла раму. Долго! ",
             "Кое-где кое-кто кое-что не решил..."]
    flag = True
    try:
        for test in tests:
            assert strip_punctuation_ru(test) == good_strip_punct(test)
    except AssertionError as e:
        flag = False

    print('YES' if flag else 'NO')
