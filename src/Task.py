import pandas
import numpy


class Task:
    def __init__(self, accuracy):
        self.eps = accuracy
        self.matrix = None
        self.solved = False

    def is_solved(self):
        return self.solved

    def set_matrix(self, matrix):
        self.matrix = matrix
