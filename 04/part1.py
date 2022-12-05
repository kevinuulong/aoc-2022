import re

input = open('input.txt')

overlaps = 0

for line in input:
    ranges = re.split(',|-', line.strip())
    a, b = set(range(int(ranges[0]), int(ranges[1]) + 1)), (range(int(ranges[2]), int(ranges[3]) + 1))

    if a.issubset(b) or a.issuperset(b):
        overlaps += 1

print(overlaps)
