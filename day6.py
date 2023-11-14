#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 6: Tuning Trouble

Task: 
How many characters need to be processed before the first start-of-packet marker is detected?

Part 2: 
How many characters need to be processed before the first start-of-message marker is detected?

For full description see:
https://adventofcode.com/2022/day/6

Input file available at:
https://adventofcode.com/2022/day/6/input

"""

def containsrepeats(s):
    """Whether the given string contains any character that is repeated.
    """
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return True
    return False

def find_marker(s, marker_len):
    """Find the marker string in a longer string.
    
    Args:
      s (str): the string where the first marker sequence is searched for
      marker_len (int): how long the marker sequence is
    
    Returns:
      int: The character position after the first marker is found in the text.
    """
    for i in range(len(s)):
        subtext = s[i:i+marker_len]
        if not containsrepeats(subtext):
            return i+marker_len


# The input file is just 1 line here.
fin = open("day6-input.txt", 'r')
text = fin.read()
print("The answer for Part 1: ", find_marker(text,4))
print("The answer for Part 2: ", find_marker(text,14))

