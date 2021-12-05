#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import functools
import itertools
import pprint

def parse_file(f):
    numbers = f.readline().split(",")
    numbers = map(int, numbers)

    f.readline() # empty line
    
    boards = []
    board = parse_board(f)
    while (len(board) > 0):
        boards.append(board)
        board = parse_board(f)
        
    return numbers, boards
    
def parse_board(f):
    board = []
    for line in f:
        numbers = line.split()
        if (len(numbers) == 0):
            break
        numbers = map(int, numbers)
        board.append(list(numbers))
    return board

    
def play(numbers, boards):
    for num in numbers:
        print("calling number", num)
        winning_boards = []
        for b in boards:
            for line in b:
                try:
                    idx = line.index(num)
                    line[idx] = -line[idx] - 1
                except ValueError:
                    pass
            # we need to store the winning board to complete marking numbers
            if win_state(b):
                winning_boards.append(b)
        if len(winning_boards) > 0:
            return winning_boards, num


def win_state(board):
    for line in board:
        if all(map(lambda n: n < 0, line)):
            return True
    for idx in range(len(board[0])):
        column = [board[line][idx] for line in range(len(board))]
        if all(map(lambda n: n < 0, column)):
            return True
    return False

def sum_unmarked(board):
    return functools.reduce(lambda x, y: x + ((y >= 0) * y),
                            itertools.chain(*board), 0)


if "__main__" == __name__:
    f = open("input")
    numbers, boards = parse_file(f)
    [win], called = play(numbers, boards)
    pprint.pp(win)
    unmarked = sum_unmarked(win)
    print("sum unmarked: ", unmarked)
    print("called: ", called)
    print("mul: ", called * unmarked)
