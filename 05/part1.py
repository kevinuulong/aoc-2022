import re

input = open('input.txt').read()

crates, instructions = input.split('\n\n')

crate_list = []

for crate in crates.split('\n')[:-1]:
    crate_list.append(re.findall(r".{1}(.).{1,2}", crate))
    
crate_list = list(zip(*crate_list))

for i, stack in enumerate(crate_list):
    crate_list[i] = [j for j in stack if j != ' ']


instructions = instructions.split('\n')

for line in instructions:
    instruction = *map(int, re.findall('\d+', line)),

    for i in range(instruction[0]):
        crate_list[instruction[2]-1].insert(0, crate_list[instruction[1]-1].pop(0))

out = ""

for stack in crate_list:
    out += stack[0]

print(out)