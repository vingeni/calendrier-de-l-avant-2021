#!/usr/bin/python3
# -*- mode: python-mode; python-shell-interpreter: "python3" -*-

import sys

def most_common_bit(values, pos):
    ones = 0
    for v in values:
        ones = ones + (v[pos] == "1")
    return str(int(ones >= (len(values) / 2)))

def least_common_bit(values, pos):
    c = most_common_bit(values, pos)
    return str(int(c == '0'))

def calculate_indicator(values, bitselector):
    position = 0
    while len(values) > 1:
        filter_bit = bitselector(values, position)
        values = [v for v in values if v[position] == filter_bit]
        position = position + 1
    return values.pop()

if __name__ == "__main__":
    values = []

    #myinput = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    myinput = open("input")

    for line in myinput:
        values.append(line)

    oxygen = int(calculate_indicator(values[:], most_common_bit), 2)
    print("oxygen:", oxygen)


    co2 = int(calculate_indicator(values[:], least_common_bit), 2)
    print("co2:", co2)

    print("multiply:", co2 * oxygen)

