#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 3: Rucksack Reorganization

Task: 
What is the sum of the priorities of items in both compartments of rucksacks?

For full description see:
https://adventofcode.com/2022/day/3

Input file available at:
https://adventofcode.com/2022/day/3/input
"""

def find_common_char(str1, str2):
    for char in str1:
        if char in str2:
            return char
            
def find_common_char3(str1, str2, str3):
    for char in str1:
        if (char in str2) and (char in str3):
            return char

# The task assigns values 1-26 to letters a-z, and 27-52 to A-Z,
# so the letter-to-int conversion of built-in ord() needs some adjustment
def convert_letter_to_priornum(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

sum_priors = 0

with open('day3-input.txt', 'r') as fin:
    for line in fin:
        line = line.strip()
        linelen = len(line)
        if linelen != 0:
            halfpt = int(linelen//2)
            char = find_common_char(line[:halfpt], line[halfpt:])
            sum_priors += convert_letter_to_priornum(char)

print("The sum of priorities of duplicate rucksack items:", sum_priors)

# Part 2 of Day 3

sum_priors2 = 0

with open('day3-input.txt', 'r') as fin:
    for line in fin:
        rucksack1 = line.strip()
        if len(rucksack1) > 0:
            rucksack2, rucksack3 = next(fin).strip(), next(fin).strip()
            char = find_common_char3(rucksack1, rucksack2, rucksack3)
            sum_priors2 += convert_letter_to_priornum(char)

print("The resulting sum of priors for the 2nd half:", sum_priors2)

