#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 10: Cathode-Ray Tube

Part 1: What is the sum of these six signal strengths?

Part 2: 

What eight capital letters appear on your CRT?

For full description see:
https://adventofcode.com/2022/day/10

Input file available at:
https://adventofcode.com/2022/day/10/input

"""

# Initialising / resetting to starting state
def reset():
    global x, cycle
    x, cycle = 1, 0 

# Functions for Part 1:

def signal_strength():
    global cycle, x, result, interesting_cycles
    if cycle in interesting_cycles:
        result += cycle * x


def noop():
    global cycle
    cycle += 1
    signal_strength()

def addx(val):
    global cycle, x
#    global x
    cycle += 1
    signal_strength()
    cycle += 1
    signal_strength()
    x += val

# for Part 2:

class Screen:
    def __init__(self):
        self.screen = [['.' for i in range(40)] for j in range(6) ]
    
    def __str__(self):
        text = ""
        for i in range(6):
            text += "".join(self.screen[i]) + "\n"
        return text

    def draw_pixel(self, cycle, x):
        row = (cycle-1) // 40
        pos = (cycle-1) % 40
        if (x - 1 <= pos <= x + 1):
            self.screen[row][pos] = "#"

def noop_and_draw():
    global cycle, x, screen
    cycle += 1
    screen.draw_pixel(cycle, x)

def addx_and_draw(val):
    global cycle, x, screen
    cycle += 1
    screen.draw_pixel(cycle, x)
    cycle += 1
    screen.draw_pixel(cycle, x)
    x += val


# The main program:

reset()
interesting_cycles = [c for c in range(20, 221, 40)] 
result = 0

fin = open("day10-input.txt", "r")

for line in fin:
    line = line.strip()
    if line != '':
        if line == "noop":
            noop()
        else:
            num = int(line.split()[1])
            addx(num)

fin.close()

print("The result for Part 1:", result)

# Part 2:
 
reset()
screen = Screen()

fin = open("day10-input.txt", "r")

for line in fin:
    line = line.strip()
    if line != '':
        if line == "noop":
            noop_and_draw()
        else:
            num = int(line.split()[1])
            addx_and_draw(num)
        
fin.close()

print("For Part 2, see the screen:\n\n" + str(screen))

