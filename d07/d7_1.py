#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

def parse_file(f):
    return list(map(int, f.readline().split(",")))



if "__main__" == __name__:

    f = open("input")
    data = parse_file(f)
    median = sorted(data)[len(data) // 2]
    cost = sum(map(lambda x: max(x, median) - min(x, median), data))

    print("cost:", cost)
