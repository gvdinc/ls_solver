# Grebenkin Vadim Variant 4
from src.FMenu import FMenu
from src.Solver import Solver
from src.Task import Task


def main():
    menu = FMenu()
    matrix = menu.choose_file()
    accuracy = 0.01  # float(input("Input accuracy: "))
    solver = Solver(Task(matrix, accuracy))
    res = solver.solve_ls()
    if res is not None:
        res.print_solution()
    return 0


if __name__ == "__main__":
    main()
