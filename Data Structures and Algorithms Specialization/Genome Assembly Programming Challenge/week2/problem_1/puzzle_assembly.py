# python3

import sys
from itertools import permutations
from copy import deepcopy


class PuzzleAssembly:
    # up: 0
    # left: 1
    # down: 2
    # right: 3
    def __init__(self):
        n, blocks = self._input()
        ans = self.solve(n, blocks)
        self.print_result(ans, blocks)

    @staticmethod
    def _input():
        data = sys.stdin.read().strip().split('\n')
        n = int(len(data) ** 0.5)
        blocks = [el[1:-1].split(',') for el in data]
        return n, blocks

    @staticmethod
    def solve(n, blocks):
        ans = [[None for _ in range(n)] for __ in range(n)]
        border = [[] for _ in range(4)]
        edge = [[0 for _ in range(2)] for __ in range(4)]  # up, left, down, right
        for i in range(len(blocks)):
            if blocks[i][0] == 'black':
                if blocks[i][1] == 'black':
                    ans[0][0] = i
                    edge[0][0] = i
                    edge[1][0] = i
                elif 'black' == blocks[i][3]:
                    ans[0][n - 1] = i
                    edge[0][1] = i
                    edge[3][0] = i
                else:
                    border[0].append(i)
            elif 'black' == blocks[i][2]:
                if 'black' == blocks[i][1]:
                    ans[n - 1][0] = i
                    edge[1][1] = i
                    edge[2][0] = i
                elif 'black' == blocks[i][3]:
                    ans[n - 1][n - 1] = i
                    edge[2][1] = i
                    edge[3][1] = i
                else:
                    border[2].append(i)
            elif 'black' == blocks[i][1]:
                border[1].append(i)
            elif 'black' == blocks[i][3]:
                border[3].append(i)

        idx = [(1, 3), (0, 2), (1, 3), (0, 2)]  # по каким граням соединяем
        # координаты border
        # для n = 3
        # [[(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0)],
        # [(2, 0), (2, 1), (2, 2)], [(0, 2), (1, 2), (2, 2)]]
        idx2 = [list(zip([0] * n, range(n))),
                list(zip(range(n), [0] * n)),
                list(zip([n - 1] * n, range(n))),
                list(zip(range(n), [n - 1] * n))]

        for i in range(4):
            for p in permutations(border[i]):
                p = [edge[i][0]] + list(p) + [edge[i][1]]
                for j in range(n - 1):
                    if blocks[p[j]][idx[i][1]] != blocks[p[j + 1]][idx[i][0]]:
                        break
                else:
                    for j in range(n):
                        ans[idx2[i][j][0]][idx2[i][j][1]] = p[j]
                    break

        solved = []
        for a in ans:
            solved.extend([el for el in a if el is not None])

        unsolved = [i for i in range(len(blocks)) if i not in solved]

        # все внутренние индексы
        _idx3 = list(zip(sum([[i] * (n - 2) for i in range(1, n - 1)], []),
                         sum([list(range(1, n - 1)) for _ in range(n - 2)], [])))

        f = lambda x: [(x[0] - 1, x[1], 2, 0),  # верхний сосед
                       (x[0], x[1] - 1, 3, 1),  # левый сосед
                       (x[0] + 1, x[1], 0, 2),  # нижний сосед
                       (x[0], x[1] + 1, 1, 3)]  # правый сосед

        idx3 = [f(x) for x in _idx3]

        for p in permutations(unsolved):
            trial = deepcopy(ans)
            # заполнили внутренние позиции
            for i in range(len(p)):
                trial[_idx3[i][0]][_idx3[i][1]] = p[i]
            is_correct = True
            for i in range(len(p)):
                for j in range(4):
                    if blocks[trial[idx3[i][j][0]][idx3[i][j][1]]][idx3[i][j][2]] != blocks[p[i]][idx3[i][j][3]]:
                        is_correct = False
                        break
                if not is_correct:
                    break
            if is_correct:
                ans = trial
                break
        return ans

    @staticmethod
    def print_result(ans, block):
        for i, a in enumerate(ans):
            print(';'.join(['(' + ','.join(block[ans[i][j]]) + ')' for j in range(len(ans))]))


if __name__ == '__main__':
    PuzzleAssembly()
