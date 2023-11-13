#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
Day 4: Camp Cleanup

Task: 
In how many assignment pairs does one range fully contain the other?

For full description see:
https://adventofcode.com/2022/day/4

Input file available at:
https://adventofcode.com/2022/day/4/input
"""

def section_to_ints(s):
    """
    input: section defined as string x-y, like 12-42
    output: the two numbers as int
    """
    s1, s2 = s.split("-")
    return int(s1), int(s2)

def contains(s, t):
    """Checks whether section s fully contains section t
    
    Args:
      s, t string: sections as described in task, e.g. 8-42
    Returns:
      bool
    """
    s0, s1 = section_to_ints(s)
    t0, t1 = section_to_ints(t)
    result = (s0 <= t0) and (s1 >= t1)
    return result

def contains_either_dir(s1, s2):
    """In a pair of sections, whether either of them fully contains the other
    """
    return contains(s1, s2) or contains(s2, s1)

def overlap(s, t):
    """Checks whether there is an overlap between two sections.
    
    Args:
      s, t string: two sections as string
    Returns:
      bool
    """
    s0, s1 = section_to_ints(s)
    t0, t1 = section_to_ints(t)
    result = ((s0 <= t0) and (s1 >= t0)) or ((t0 <= s0) and (t1 >= s0))
    return result

# the counter for Part 1
ct = 0

# the counter for Part 2
ct_overlap = 0

#with open("day4-smallinput.txt", 'r') as file:
with open("day4-input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if len(line) > 0:
            half1, half2 = line.split(",")
            
            # for Part 1:
            if contains_either_dir(half1, half2):
                ct += 1
            
            # for Part 2: 
            if overlap(half1, half2):
                ct_overlap += 1
            
# the answer for Part 1
print("The number of pairs where one range fully contains the other one:", ct)

# the answer for Part 2
print("The number of pairs where the two ranges overlap:", ct_overlap)

