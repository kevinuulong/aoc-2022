input = open('input.txt').read()
input = input.split('\n\n')

calories = []

for elf in input:
    elf = map(lambda s: int(s), elf.split('\n'))
    calories.append(sum(elf))

top_3 = sorted(calories, reverse=True)[:3]

print(sum(top_3))