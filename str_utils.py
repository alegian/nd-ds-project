import numpy

alphabet = ' abcdefghijklmnopqrstuvwxyz'


def enbase(x):
    x = int(x)
    n = len(alphabet)
    if x < n:
        return alphabet[x]
    return enbase(x / n) + alphabet[x % n]


def debase(x):
    n = len(alphabet)
    result = 0
    for i, c in enumerate(reversed(x)):
        result += alphabet.index(c) * (n ** i)
    return result


def pad(x, n):
    p = alphabet[0] * (n - len(x))
    return '%s%s' % (x, p)


def str_average(a, b):
    n = max(len(a), len(b))
    a = debase(pad(a, n))
    b = debase(pad(b, n))
    return enbase((a + b) / 2)


def str_diff_norm_squared(a, b):
    exponent = 5
    diff = []

    max_len = max(len(a), len(b))
    a = a.ljust(max_len, ' ')
    b = b.ljust(max_len, ' ')

    for i, c in enumerate(a):
        idx1 = alphabet.index(c)
        idx2 = alphabet.index(b[i])
        diff.append((idx1-idx2)*(24**exponent))
        exponent = exponent - 1

    return numpy.linalg.norm(diff)
