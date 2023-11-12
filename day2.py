#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Task:
Calculate the score of a row of Rock-Paper-Scissors games.

For full description see:
https://adventofcode.com/2022/day/2

Input file available at:
https://adventofcode.com/2022/day/2/input
"""

# to build and use the evaluation table in a simple way
import pandas as pd

"""
Part 1
------
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors

Scoring:
the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
and 0 if you lost, 3 if the round was a draw, and 6 if you won

   X  Y  Z
A  4  8  3
B  1  5  9
C  7  2  6

The table is stored and uploaded in the file:
day2-evaltable.csv

The Pandas DataFrame makes it easy to use the matrix with the given letters.
"""

score = 0

evalsheet = pd.read_csv('day2-evaltable.csv', index_col = 0)

def game_eval(you, me):
    return evalsheet.loc[you][me]

with open("day2-input.txt", "r") as file: 
    for line in file:
        line = line.strip()
        if line != "":
            you, me = line.split()
            score_round = game_eval(you, me)
            score += score_round

print("In the end, my score is:", score)

"""
Part 2

amend: 
X means you need to lose, Y means you need to end in a draw, and Z means you need to win.
A rock 1 pt, B paper 2 pt, C scissors 3 pt

The amended evaluation table:
   lose  draw   win
   X     Y      Z
A  C-3   A-4    B-8
B  A-1   B-5    C-9
C  B-2   C-6    A-7

The point scoring system is stored and uploaded in:
day2-evaltable-amend.csv

The implementation remains the same.
Use the amended csv file with the new scoring system, in the code above.

evalsheet = pd.read_csv('day2-evaltable-amend.csv', index_col = 0)
"""

