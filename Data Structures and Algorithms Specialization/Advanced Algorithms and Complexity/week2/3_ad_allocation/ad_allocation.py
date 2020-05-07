# python3
from sys import stdin

epsilon = 1e-7


def allocate_ads(n, m, A, b, c):
    Big = 1e7
    z = []
    ans = 0
    solu = [0 for _ in range(m)]
    basic = []
    for i in range(m):
        z.append(-c[i])
    lt = []
    af = []
    count = m
    for i in range(n):
        if b[i] < -epsilon:
            b[i] = -b[i]
            for j in range(len(A[i])):
                A[i][j] = -A[i][j]
            lt.append(i)
            z.append(0)
            z.append(Big)
            solu.append(0)
            solu.append(b[i])
            basic.append(count + 1)
            af.append(count + 1)
            count += 2
            for j in range(n):
                if i == j:
                    A[j].append(-1)
                    A[j].append(1)
                else:
                    A[j].append(0)
                    A[j].append(0)
        else:
            z.append(0)
            solu.append(b[i])
            basic.append(count)
            count += 1
            for j in range(n):
                if i == j:
                    A[j].append(1)
                else:
                    A[j].append(0)
    for i in lt:
        scale = Big
        ans = ans - b[i] * scale
        for j in range(len(z)):
            z[j] = z[j] - A[i][j] * scale
    while any(z[i] < -epsilon for i in range(len(z))):
        piv_element = z.index(min(z))
        rmin = 1e9
        index = -1
        for i in range(n):
            if A[i][piv_element] > epsilon:
                r = b[i] / A[i][piv_element]
                if r < rmin:
                    rmin = r
                    index = i
        if index == -1:
            return (1, [0] * m)
        scale = A[index][piv_element]
        b[index] /= scale
        for i in range(len(A[index])):
            A[index][i] /= scale
        if abs(z[piv_element]) > epsilon:
            scale = z[piv_element]
            ans = ans - b[index] * scale
            for i in range(len(A[index])):
                z[i] = z[i] - A[index][i] * scale
        for i in range(n):
            if i == index or abs(A[i][piv_element]) < epsilon:
                continue
            else:
                scale = A[i][piv_element]
                b[i] = b[i] - b[index] * scale
                for j in range(len(A[i])):
                    A[i][j] = A[i][j] - A[index][j] * scale
        solu[piv_element] = b[index]
        solu[basic[index]] = 0
        basic[index] = piv_element

    for i in range(n):
        solu[basic[i]] = b[i]
    if any(solu[i] < -epsilon for i in range(n + m)) or (len(af) > 0 and any(solu[i] > epsilon for i in af)):
        return (-1, solu[0:m])
    return (0, solu[0:m])


n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = allocate_ads(n, m, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
