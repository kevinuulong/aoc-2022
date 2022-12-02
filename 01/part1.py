input = open('input.txt').read()
input = input.split('\n\n')

calories = []

for elf in input:
    elf = map(lambda s: int(s), elf.split('\n'))
    calories.append(sum(elf))

print(max(calories))