#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 7: No Space Left On Device

Task 1: What is the sum of the total sizes of those directories?

For full description see:
https://adventofcode.com/2022/day/7

Input file available at:
https://adventofcode.com/2022/day/7/input

"""

import re

# The cd command is used to jump up/down 1 level in the file tree,
# hence the path to dirs and subdirs can be stored in a stack
dirstack = []

# The dict keys will be the paths to dirs (converted to string)
dirsizes = {}

fin = open("day7-input.txt", "r")

for line in fin:
    line = line.strip()
    if line != "":
    
        if re.match(r'\$ cd', line):
            dirname = line.split()[-1]
            if dirname == "..":
                dirstack.pop()
            else:
                dirstack.append(dirname)
                
                # the stack is a list, that can't be keys in a dict
                filepath = '/'.join(dirstack)
                
                if filepath not in dirsizes:
                    dirsizes[filepath] = 0
            
        elif re.match(r'\d+', line):
            filesize = int(line.split()[0])
            filepath = '/'.join(dirstack)

            # sizes are added to all dirs that directly or indirectly contain the file
            for key in dirsizes:
                if re.match(key, filepath):
                    dirsizes[key] += filesize


answer1 = 0

for key, value in dirsizes.items():
    if value < 100000:
        answer1 += value

print("The answer for part 1:", answer1)

# Part 2

# size needed: space needed for update minus the currenty free space 
size_needed = 30000000 - (70000000 - dirsizes["/"])

# searching for the min value that is above size_needed
enough_size = 70000000

for key, value in dirsizes.items():
    if (value < enough_size) and (value >= size_needed ):
        enough_size = value

print("The answer for Part 2:", enough_size)

