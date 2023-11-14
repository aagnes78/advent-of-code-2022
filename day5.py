#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 5: Supply Stacks

Task: After the rearrangement procedure completes, what crate ends up on top of each stack?

For full description see:
https://adventofcode.com/2022/day/5

Input file available at:
https://adventofcode.com/2022/day/5/input

The stacks of crates look like:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Instructions look like:

"move 2 from 2 to 1"

"""

import re

class Stacks:
    def __init__(self, number=1):
        self._number_of_stacks = number
        self.stacksdict = {i+1 : [] for i in range(number)}
    
    def add_one_crate(self, stack, crate):
        self.stacksdict[stack].append(crate)
    
    def crates_on_top(self):
        top =""
        for i in range(self._number_of_stacks):
            if len(self.stacksdict[i+1]) == 0:
                top += "_"
            else:
                top += self.stacksdict[i+1][-1]
        return top
    
    # for Part 1
    def move_one_crate(self, stack_from, stack_to):
        crate = self.stacksdict[stack_from].pop(-1)
        self.stacksdict[stack_to].append(crate)
    
    def move_crates(self, amount, stack_from, stack_to):
        for i in range(amount):
            self.move_one_crate(stack_from, stack_to)
    
    # for Part 2
    def cratemover9001(self, amount, stack_from, stack_to):
        crates = self.stacksdict[stack_from][-amount:]
        self.stacksdict[stack_to].extend(crates)
        del self.stacksdict[stack_from][-amount:]
    

def stackbuilder(text):
    """Builds stacks from text input.

    Args:
      text (str): a bunch of stacks in a multiline string

    Returns:
      Stacks: a Stacks object built from the input string
    """
# The stacks given in string input look like:
#            [D]    
#        [N] [C]    
#        [Z] [M] [P]
#         1   2   3 
    lines = text.splitlines()
    # the number of stacks is the last number in the text
    find_num = re.findall(r'(\d)\D+$', lines[-1])
    num = int(find_num[0])
    stacks = Stacks(num)
     
    # reversing just to make traversing the lines easier
    lines.reverse()
    for line in lines:
        if re.match(r'.*\[', line):
            for k in range(num):
                ind = k*4 + 1
                c = line[ind]
                # if column is not high enough, ignore c
                if c.isupper():
                    stacks.add_one_crate(k+1, c)
    return stacks
    

def follow_move_instructions(stacks, func, line):
    """Apply function on stacks, based on instructions in text.
    
    Args:
      stacks (Stacks): Stacks object
      func: a Stacks method, to be applied on stacks
      line (str): instructions with the patterb:
        "move 2 from 3 to 5"
    
    Returns:
      Stacks: the input object altered by the applied method
    """
    if "move" in line:
        nums = (re.findall(r"move\s(\d+)\sfrom\s(\d+)\s+to\s+(\d+)", line))
        func(int(nums[0][0]), int(nums[0][1]), int(nums[0][2]))


file = open("day5-input.txt", "r")
biginput = file.read()
file.close()

# input includes the stacks and list of moves, separated by empty line
input_blocks = biginput.split("\n\n")
instructions = input_blocks[1].splitlines()


# Part 1: 
print("Part 1:")
stacks = stackbuilder(input_blocks[0])

for line in instructions:
    follow_move_instructions(stacks, stacks.move_crates, line)

print("What crate ends up on top of each stack?", stacks.crates_on_top())


# Part 2
print("\nPart 2:")

# recreating the starting state of the stacks
stacks = stackbuilder(input_blocks[0])

for line in instructions:
    follow_move_instructions(stacks, stacks.cratemover9001, line)

print("The top of the stacks, if the crane can move multiple crates:", 
      stacks.crates_on_top())

