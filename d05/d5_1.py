#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import itertools
import pprint

def parse_file(f):
    vents = []
    size = 0
    for line in f:
        coords = line.split(" -> ")
        (x1, y1) = coords[0].split(',')
        (x2, y2) = coords[1].split(',')
        vents.append((int(x1),int(y1),int(x2),int(y2)))
        size = max(size, max(vents[-1]))
    return vents, size + 1


def create_diagram(size):
    diagram = []
    for y in range(size):
        diagram.append([0 for i in range(size)])
    return diagram


def draw_vent(diagram, vent, only_horizontal):

    x1, y1, x2, y2 = vent

    if only_horizontal and not (x1 == x2 or y1 == y2):
        return diagram

    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            diagram[y][x1] += 1
    elif (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            diagram[y1][x] += 1
    else:
        dx = dy = 1
        if y2 < y1:
            dy = -1
        if x2 < x1:
            dx = -1
        x = x1
        for y in range(y1, y2 + dy, dy):
            diagram[y][x] += 1
            x += dx
            
    return diagram



def count_override(diagram):
    flat = itertools.chain(*diagram)
    return sum(1 for _ in filter(lambda n: n > 1, flat))


if "__main__" == __name__:

    f = open("small")
    vents,size = parse_file(f)

    diagram = create_diagram(size)
    for v in vents:
        diagram = draw_vent(diagram, v, True)

    #pprint.pp(diagram)
    print("override:", count_override(diagram))
