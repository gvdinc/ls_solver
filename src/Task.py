import pandas
import numpy


class Task:
    def __init__(self, matrix, accuracy):
        self.eps = accuracy
        self.matrix = matrix
        self.solved = False

    def is_solved(self):
        return self.solved

    def set_matrix(self, matrix):
        self.matrix = matrix
