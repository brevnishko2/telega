import re
import random


def get_text(fname):
    a = r'".+"'
    with open(fname, encoding='utf-8') as inf:
        text = inf.read()

    res = re.findall(a, text)
    return [x.replace('"', '') for x in res]


def add_brat(lst):
    result = []
    for phrase in lst:
        phrase = phrase.split()
        ln = len(phrase)
        ind = random.randint(0, ln)
        if ind == 0:
            brat = 'Брат, '
        else:
            brat = ', Брат,'
        phrase.insert(ind, brat)
        phrase = ' '.join(phrase)
        result.append(phrase)
    return result
