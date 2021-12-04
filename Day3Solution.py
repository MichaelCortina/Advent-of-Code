from Utilities import *

gamma_rate = epsilon_rate = ""
num = 0
input = ["" for i in range(0,12)]
with open('Day3Input.txt') as f:
    contents = f.read().replace("\n","")
for i in range(0, len(contents)):
    input[num] += contents[i]
    num += 1
    if num >= len(input):
        num = 0
for s in input:
    if s.count('1') > s.count('0'):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
print(int(gamma_rate, 2) * int(epsilon_rate, 2))