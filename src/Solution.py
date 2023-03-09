class Solution:
    def __init__(self, is_solved, x_k, deltas):
        self.is_solved = is_solved
        self.x_k = x_k
        self.deltas = deltas
        self.iteration_number = len(x_k) - 1

    def print_solution(self):
        print("result:")
        for i in range(len(self.x_k)):
            print(i, end=") ")
            for x in self.x_k[i]:
                print(round(x, i+2), end=" ")
            print(round(self.deltas[i], i+2))
        print('\n', end='')
        print("finished in ", self.iteration_number, " iterations")
