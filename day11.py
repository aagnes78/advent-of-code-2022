#!/usr/bin/env python3
# -*-coding: utf-8 -*-

"""
Day 11: Monkey in the Middle

What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

For full description see:
https://adventofcode.com/2022/day/11

Input file available at:
https://adventofcode.com/2022/day/11/input

Part 2 would generate very very large numbers, so simulation is implemented with a trick.
(Based on modular arithmetic, the test input and puzzle input would use different mod number.)

"""

from collections import deque
import re

class Monkey:
    """A Monkey as defined in the task description
    
    Attributes:
      name (str): not really necessary
      items (collection.deque): the items with an int as the worry level, in a FIFO
      op (func): the operation the given monkey does when "inspecting" an item
      div_num (int): before throwing an item, the monkey checks 
        whether the "worry level" is divisible by this number
      monkey_yes (int): throw item to this monkey if divisibility condition is true
      monkey_no (int): throw item to this monkey if divisibility condition is false
      inspect_ct (int): the number of inspection the monkey performs
        set to 0 when Monkey is created (i.e. at the beginning of the game)
    
    Methods:
      
    """
    def __init__(self, name, items, opfunc, div_num, monkey_yes, monkey_no):
        self.name = name
        self.items = deque(items)
        self.op = opfunc
        self.div_num = div_num
        self.monkey_yes = monkey_yes
        self.monkey_no = monkey_no
        self.inspect_ct = 0
        
    def __str__(self):
        return self.name + " has: " + str(list(self.items)) + " inspected: " + str(self.inspect_ct)
    
    def throw_item(self, item, other_monkey):
        other_monkey.receive_item(item)
    
    def receive_item(self, item):
        self.items.append(item)

    def inspect_next(self, part):
        item = self.items.popleft()
        item = self.op(item)
        
        # part 1 vs part 2
        if part == 1:
            item = item // 3
        else:
            item = item % 9699690
            # but use this for the test input:
            # item = item % 96577

        if item % self.div_num == 0:
            self.throw_item(item, monkeys[self.monkey_yes])
        else:
            self.throw_item(item, monkeys[self.monkey_no])
        
    def inspect_items(self, part):
        if len(self.items) > 0:
            for i in range(len(self.items)):
                self.inspect_next(part)
                self.inspect_ct += 1


def monkey_parser(text):
    # The description for all monkeys is given in a set format.
    lines = text.splitlines()
    name = re.findall(r'\d+', lines[0])[0]
    items = lines[1].strip().split(' ')[2:]
    items = [int(re.sub(r',', '', x)) for x in items]
    div_num = re.findall(r'\d+', lines[3])[0]
    monkey_yes = re.findall(r'\d+', lines[4])[0]
    monkey_no = re.findall(r'\d+', lines[5])[0]
    optype = lines[2].strip().split(' ')[-2]
    opnum = lines[2].strip().split(' ')[-1]

    if optype == '+':
        func = lambda x: x + int(opnum)
    else:
        if opnum == "old":
            func = lambda x: x * x
        else:
            func = lambda x: x * int(opnum)

    return name, items, func, int(div_num), int(monkey_yes), int(monkey_no)


def monkey_setup(monkeys, allinfo):
    for i in range(len(allinfo)):
        if allinfo[i] != '':
            monkeys.append(Monkey(*monkey_parser(allinfo[i])))


def monkey_business(monkeys, n, part):
    """Simulating n rounds of monkey business, for either Part 1 or 2
    """
    for i in range(n):
        for monkey in monkeys:
            monkey.inspect_items(part)


def inspection_calculator(monkeys):
    counterlist = []
    for monkey in monkeys:
        counterlist.append(monkey.inspect_ct)
    
    counterlist.sort()
    return counterlist[-1] * counterlist[-2]


# The main program for the task:

file = open("day11-input.txt", 'r')
allinfo = file.read().split("\n\n")
file.close()

# Part 1

monkeys = []
monkey_setup(monkeys, allinfo)

monkey_business(monkeys, 20, 1)
result = inspection_calculator(monkeys)

print('Part 1\n  after 20 rounds of stuff-slinging simian shenanigans:', result)


# Part 2

# recreating the starting position
monkeys = []
monkey_setup(monkeys, allinfo)

monkey_business(monkeys, 10000, 2)
result = inspection_calculator(monkeys)

print('Part 2\n  after 10000 rounds of stuff-slinging simian shenanigans:', result)

