#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import itertools

def parse_file(f):
    state = f.readline().split(',')
    return map(lambda s: int(s), state)

def sim(state):
    nchildren = sum(1 for _ in filter(lambda s: s == 0, state))
    state = map(lambda s: 6 if s == 0 else s - 1, state)
    return itertools.chain(state, itertools.repeat(8, nchildren))

if "__main__" == __name__:

    f = open("input")
    state = list(parse_file(f))

    print("Initial state:", list(state))
    for d in range(80):
        state = list(sim(state))
        print("After {:2} days: {}".format(d + 1, len(state)))
        
