#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 9: Rope Bridge

Task: How many positions does the tail of the rope visit at least once?

For full description see:
https://adventofcode.com/2022/day/9

Input file available at:
https://adventofcode.com/2022/day/9/input

"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def get_pos(self):
        return self.x, self.y
    
    def move(self, direction):
        step_options = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0), 
                        "UL": (1, -1), "UR": (1, 1), "DL": (-1, -1), "DR": (-1, 1)}
        self.x += step_options[direction][0]
        self.y += step_options[direction][1]
    
    def follow(self, head):
        if (abs(self.x - head.x) <= 1) and (abs(self.y - head.y) <= 1):
            pass
            
        elif (abs(self.x - head.x) == 2) and (abs(self.y - head.y) < 2):
            # moving 1 step in pos or neg direction
            self.x += (head.x - self.x) // 2
            self.y = head.y
        
        elif (abs(self.x - head.x) < 2) and (abs(self.y - head.y) == 2):
            # moving 1 step in pos or neg direction
            self.y += (head.y - self.y) // 2
            self.x = head.x
        
        elif (abs(self.x - head.x) == 2) and (abs(self.y - head.y) == 2):
            self.x += (head.x - self.x) // 2
            self.y += (head.y - self.y) // 2


# for Part 1:
def move_n_times(direction, n):
    for i in range(n):
        head.move(direction)
        tail.follow(head)
        visited.add(tail.get_pos())


# for Part 2:
def move_rope(direction, n):
    for i in range(n):
        head.move(direction)
        tail[0].follow(head)
        for knot in range(1, 9):
            tail[knot].follow(tail[knot-1])
        visited.add(tail[8].get_pos())
        

# Part 1

head, tail = Point(), Point()
visited = set()

fin = open("day9-input.txt", "r")
for line in fin:
    line = line.strip()
    if line != "":
        letter = line.split()[0]
        n = int(line.split()[1])
        move_n_times(letter, n)
        
fin.close()

print("Part 1: The number of points visited:", len(visited))

# Part 2

head = Point()

# the tail of the rope is a list of 9 points, the end of tail is tail[8]
tail = [Point() for i in range(9)]

visited = set()

fin = open("day9-input.txt", "r")
for line in fin:
    line = line.strip()
    if line != "":
        letter = line.split()[0]
        n = int(line.split()[1])
        move_rope(letter, n)
        
fin.close()

print("Part 2: The number of points visited:", len(visited))

