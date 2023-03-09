# Grebenkin Vadim Variant 4
from src.FMenu import FMenu
from src.Solver import Solver
from src.Task import Task


def main():
    accuracy = float(input("Input accuracy: "))
    manual = input("use manual mode? Y/N: ")
    if manual.lower().strip() == 'n':
        menu = FMenu()
        matrix = menu.choose_file()
    else:
        matrix = FMenu.type_matrix()
    solver = Solver(Task(matrix, accuracy))
    res = solver.solve_ls()
    if res is not None:
        res.print_solution()
    return 0


if __name__ == "__main__":
    main()
