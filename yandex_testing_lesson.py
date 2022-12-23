def strip_punctuation_ru(line):
#    return ' '.join(line.split())


#def good_strip_punct(line):
    text = ''.join(x for x in line if x.isalpha() or x.isspace()
                   or x == '-').replace(' - ', ' ')
    return ' '.join(text.split())
