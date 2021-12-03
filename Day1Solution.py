from Utilities import *
input = to_int("Day1Input.txt")
count = sum_count = 0
current = previous = [input[0],input[1],input[2]]
for i in range(0, len(input)):
    current[i%3] = input[i]
    if input[i] > input[i - 1]:
        count += 1
    if sum(current) > sum(previous):
        sum_count += 1
    previous = current.copy()
print(count)
print(sum_count)