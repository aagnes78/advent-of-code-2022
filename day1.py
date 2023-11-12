#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Task:
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

Detailed description:
https://adventofcode.com/2022/day/1

The input file is available there:
https://adventofcode.com/2022/day/1/input

The code below assumes it has been saved locally.
"""

# The original question did not include "which elf?",
# but if you are hungry, you might want to know where to find food :)
# I was just curious, and maybe, Part 2 would ask that.

calories = {}
elf_no = 0
prev_line = ""

fin = open("day1-input.txt", 'r')

for line in fin:
    line = line.strip()
    
    if prev_line == "":    # a new elf's calories after an empty line
        elf_no += 1
        calories[elf_no] = int(line)
    else:
        if line != "":
            calories[elf_no] += int(line)       
    prev_line = line

fin.close()

print("The highest total calory an elf is carrying:", max(calories.values()))
print("and btw, that is elf no.", max(calories, key=calories.get))


# Day 1 , Puzzle 2
# So, Part 2 didn't ask which elf carried the highest calories, either.
# Part 2: give the sum of the Top 3 calories.

calories_list = [val for key, val in calories.items()]
top3 = sum(sorted(calories_list)[-3:])

print("The calories that the top 3 elves are carrying:", top3)

