#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import itertools

def parse_file(f):
    ages = f.readline().split(',')
    ages = map(lambda s: int(s), ages)
    state = dict(enumerate([0] * 9))
    for s in ages:
        state[s] += 1
    return state

def sim(state):
    new_state = dict(enumerate([0] * 9))

    # process fishes with childrens
    new_state[6] += state[0]
    new_state[8] += state[0]

    # process other ages
    for d in range(1, 9):
        new_state[d - 1] += state[d]
        
    return new_state


def count(state):
    return sum(state.values())


if "__main__" == __name__:

    f = open("input")
    state = parse_file(f)
    sim(state)

    print("Initial state", count(state))
    for d in range(256):
        state = sim(state)
        print("After {:2} days: {}".format(d + 1, count(state)))
