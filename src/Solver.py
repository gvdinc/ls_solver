import itertools
import sys

import numpy as np
from src.Task import Task
from Solution import Solution


class Solver:
    def __init__(self, task):
        self.task = task
        self.matrix = task.matrix
        self.a = task.matrix[:, :-1]

    def solve_ls(self):
        is_transformed = self.transform_matrix()
        if not is_transformed:
            print("convergence impossible")
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

    def transform_matrix(self):
        dictionary = [set() for _ in range(len(self.a))]
        counter = 0

        # Собираем массив множеств подходящих строк
        # Собираем массив множеств подходящих строк
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                s = sum(abs(x) for x in self.a[i][:j]) + sum(abs(x) for x in self.a[i][j + 1:])
                if abs(self.a[i][j]) >= s:
                    dictionary[j].add(i)
                if abs(self.a[i][j]) > s:
                    counter += 1

        if not counter:
            return False

        if not self._check_dict(dictionary): return False

        maxi = 20
        while maxi > 2:
            max_len = 0
            for i in range(len(dictionary)):
                for j in range(len(dictionary)):
                    if i != j and len(dictionary[j]) == 1:
                        dictionary[i] = dictionary[i] - dictionary[j]
                        max_len = max(max_len, len(dictionary[i]))
            maxi = max_len

        self._check_dict(dictionary)

        for i in range(len(dictionary)):
            if len(dictionary[i]) == 2:
                dictionary[i].pop()
                for j in range(i + 1, len(dictionary)):
                    dictionary[j] = dictionary[j] - dictionary[i]

        new_matrix = []
        for position in dictionary:
            pos = (list(position)[0])
            new_matrix.append(self.matrix[pos])
        self.matrix = new_matrix
        return True

    @staticmethod
    def _check_dict(dictionary):
        for i in dictionary:
            if not i:
                return False
        return True
