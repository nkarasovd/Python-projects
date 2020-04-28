# python3
import sys


def InverseBWT(bwt):
    n = len(bwt)

    lst_2 = []

    d = {'A': 1, 'C': 1, 'G': 1, 'T': 1, '$': 1}
    for id, el in enumerate(list(bwt)):
        lst_2.append((el, d[el], id))
        d[el] += 1

    lst_1 = sorted(lst_2, key=lambda x: (x[0], x[2]))

    s = lst_1[0][0]

    i = 0
    j = lst_1[0][2]
    step = 1
    while len(s) != n:
        if step == 1:
            i = lst_2[j]
            s += lst_1[i[2]][0]
            step = 2
        else:
            j = lst_1[i[2]][2]
            step = 1
    return s[1:] + '$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
