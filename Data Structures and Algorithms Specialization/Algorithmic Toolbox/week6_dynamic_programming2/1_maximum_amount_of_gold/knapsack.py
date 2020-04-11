# Uses python3
import sys

"""
Пусть A(k,s) есть максимальная стоимость предметов, которые можно уложить в рюкзак вместимости s,
если можно использовать только первые k предметов, то есть {n1,n2,…,nk}, 
назовем этот набор допустимых предметов для A(k,s).

Если предмет k не попал в рюкзак. Тогда A(k,s) равно максимальной стоимости рюкзака с такой же вместимостью
и набором допустимых предметов {n1,n2,…,nk−1}, то есть A(k,s)=A(k−1,s). 
Если k попал в рюкзак. Тогда A(k,s) равно максимальной стоимости рюкзака, где вес s уменьшаем на вес k-ого предмета
и набор допустимых предметов {n1,n2,…,nk−1} плюс стоимость k, то есть A(k−1,s−wk)+pk
"""


def optimal_weight(W, w, n):
    # write your code here
    d = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for weight in range(1, W + 1):
            d[i][weight] = d[i - 1][weight]
            if w[i - 1] <= weight:
                val = d[i - 1][weight - w[i - 1]] + w[i - 1]
                if val > d[i][weight]:
                    d[i][weight] = val

    print(*d, sep='\n')

    return d[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
