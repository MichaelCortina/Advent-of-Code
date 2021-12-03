from Utilities import *
import re

horizontal = depth = aim = 0
with open('Day2Input.txt') as f:
    contents = f.read()
input = list(group(contents.replace("\n", " ").split(" "), 2))
for arg in input:
    if arg[0] == 'forward':
        horizontal += int(arg[1])
        depth += aim * int(arg[1])
    if arg[0] == 'down':
        aim += int(arg[1])
    if arg[0] == 'up':
        aim -= int(arg[1])
print(horizontal * depth)