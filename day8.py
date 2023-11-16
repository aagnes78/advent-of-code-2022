#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 8: Treetop Tree House

Task - Part1:
How many trees are visible from outside the trees?

For full description see:
https://adventofcode.com/2022/day/8

Input file available at:
https://adventofcode.com/2022/day/8/input

"""
import numpy as np

fin = open("day8-input.txt", 'r')

firstline = fin.readline()
firstline = firstline.strip()
size = len(firstline)

trees = np.empty(shape=(size, size))

trees[0] = [int(c) for c in firstline]

row = 1
for line in fin:
    line = line.strip()
    if len(line) > 0:
        trees[row] = [int(c) for c in line]
        row += 1

# Creating a new matrix full with 0, to mark the visible trees (with 1)
ct_matrix_np = np.array([[0 for column in range(size)] for row in range(size)])


# all the trees around the edge are visible
for column in range(size):
    ct_matrix_np[0,column] = 1
    ct_matrix_np[size-1,column] = 1

for row in range(size):
    ct_matrix_np[row, 0] = 1
    ct_matrix_np[row, size-1] = 1

# find the visible trees in the middle:
# visible from 1 direction if higher than the highest tree in that direction
for row in range(1, size-1):
    for column in range(1, size-1):
        x = trees[row,column]
        if ((x > max(trees[row,:column])) | (x > max(trees[row,column+1:]))
           | (x > max(trees[:row,column])) | (x > max(trees[row+1:,column]))):
            ct_matrix_np[row, column] = 1
    
print("The number of visible trees in the trees:", sum(sum(ct_matrix_np)))

# Part 2

# how many trees are in the view to the left/right/up/down direction from a given tree

def look_left(row, column):
    tree = trees[row, column]
    ct = 1
    next_tree = trees[row, column-ct]
    #print(next_tree)
    while ((next_tree < tree) and (column-ct > 0)):
        ct += 1
        next_tree = trees[row, column-ct]
    return ct

def look_right(row, column):
    tree = trees[row, column]
    ct = 1
    next_tree = trees[row, column+ct]
    while ((next_tree < tree) and (column+ct < size-1)):
        ct += 1
        next_tree = trees[row, column+ct]
    return ct

def look_up(row, column):
    tree = trees[row, column]
    ct = 1
    next_tree = trees[row-ct, column]
    while ((next_tree < tree) and (row-ct > 0)):
        ct += 1
        next_tree = trees[row-ct, column]
    return ct

def look_down(row, column):
    tree = trees[row, column]
    ct = 1
    next_tree = trees[row+ct, column]
    while ((next_tree < tree) and (row+ct < size-1)):
        ct += 1
        next_tree = trees[row+ct, column]
    return ct


# recreating the counter matrix with 0 everywhere
ct_matrix_np = np.array([[0 for column in range(size)] for row in range(size)])

# by definition of "view", all scores are 0 for trees on the edges of the grid
# hence the for loop starts index 1 (second row, second column)
for row in range(1, size-1):
  for column in range(1, size-1):
    x = trees[row,column]
    
    # the views from this tree, in all 4 directions:
    look1 = look_left(row, column)
    look2 = look_right(row, column)
    look3 = look_up(row, column)
    look4 = look_down(row, column)
    
    # storing the "scenic score" for this tree in the counter matrix
    ct_matrix_np[row,column] = look1 * look2 * look3 * look4


# find the highest scenic score among all the trees:
print("The highest scenic score possible for any tree:", ct_matrix_np.max())

