import argparse

from typing import Dict
from parser import Parser
from solver import Solver


def main(equation: str, verbose: bool):
    if verbose:
        print('Начинаем парсинг уравнения')
    equation_parser: Parser = Parser(equation, verbose)
    equation_parser.parse_equation()
    if verbose:
        print('Парсинг уравнения успешен')
        print('Начинаем решать уравнение')
    equation_solver: Solver = Solver(equation_parser.multipliers, verbose)
    equation_solver.solve_equation()
    if verbose:
        print('Уравнение успешно решено')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Найти все решения квадратичного или линейного уравнения.')
    parser.add_argument('equation', type=str, help='строка с уравнением')
    parser.add_argument('-v', action='store_true', help='подробный вывод')
    args = parser.parse_args()
    try:
        main(args.equation, args.v)
    except Exception as e:
        print(e)
