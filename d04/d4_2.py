#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import pprint
from d4_1 import parse_file, play, sum_unmarked


if "__main__" == __name__:
    f = open("input")
    numbers, boards = parse_file(f)

    while len(boards) > 1:
        winning_boards, called = play(numbers, boards)
        #print("removing {} winning boards".format(len(winning_boards)))
        for b in winning_boards:
            boards.remove(b)

    print("one board left...")
    [win], called = play(numbers, boards)
    pprint.pp(win)
    unmarked = sum_unmarked(win)
    print("sum unmarked: ", unmarked)
    print("called: ", called)
    print("mul: ", called * unmarked)
