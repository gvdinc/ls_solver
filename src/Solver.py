import itertools

import numpy as np
from src.Task import Task
from Solution import Solution


class Solver:
    def __init__(self, task):
        self.task = task
        self.matrix = task.matrix

    def solve_ls(self):
        self._make_convergent()
        m_size = len(self.matrix)
        C = []
        d = []
        for n in range(m_size):
            xline = np.zeros(m_size)
            for i in range(m_size + 1):
                if i != n:
                    if i < m_size:
                        xline[i] = -1 * self.matrix[n][i] / self.matrix[n][n]
                    else:
                        d.append(self.matrix[n][i] / self.matrix[n][n])
            C.append(xline)
        C = np.array(C)  # 𝒙 = 𝑪𝒙 + d

        stop_f = False
        x_k = [d]
        deltas = [1]
        while not stop_f:
            k = len(x_k) - 1
            x = np.zeros(m_size)  # x_(k+1)
            for i in range(m_size):
                summ = 0
                for j in range(m_size):
                    if j != i:
                        summ += C[i][j] * -1 * x_k[k][j]
                x[i] = d[i] - summ
            delta = max(abs(x_k[k] - x))
            x_k.append(x)
            deltas.append(delta)
            if delta < self.task.eps:
                stop_f = True
            elif k > 50:
                print("impossible")
                break
        return Solution(stop_f, x_k, deltas)

    def _make_convergent(self):
        permutations = list(itertools.permutations(self.matrix))
        for permutation in permutations:
            strict_f = False
            is_conv = True
            for i in range(len(permutation)):
                if 2 * permutation[i][i] > sum(permutation[i][0:-1]):
                    strict_f = True
                if 2 * permutation[i][i] >= sum(permutation[i][0:-1]):
                    continue
                else:
                    is_conv = False
                    break
            if is_conv and strict_f:
                print("Convergent - set to matrix:")
                for line in permutation:
                    for el in line:
                        print(el, end=' ')
                    print('')
                self.matrix = permutation
                return
        print("Not convergent")
