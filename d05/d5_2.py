#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

from d5_1 import parse_file, create_diagram, draw_vent, count_override
import pprint


if "__main__" == __name__:

    f = open("input")
    vents, size = parse_file(f)

    diagram = create_diagram(size)
    for v in vents:
        diagram = draw_vent(diagram, v, False)

    #pprint.pp(diagram)
    print("override:", count_override(diagram))
