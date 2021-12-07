#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

def parse_file(f):
    return list(map(int, f.readline().split(",")))

def cost(d):
    return d * (d + 1) // 2

if "__main__" == __name__:

    f = open("input")
    data = parse_file(f)
    avg = sum(data) // len(data)
    cost = sum(map(lambda x: cost(max(x, avg) - min(x, avg)), data))

    print("avg:", avg)
    print("cost:", cost)
