input = open('input.txt').readlines()
input = *map(lambda s: s.replace('\n', '').split(' '), input),

choices = {'A': 1, 'B': 2, 'C': 3}
condition = {'X': 1, 'Y': 0, 'Z': 2}
input = *map(lambda s: [choices[s[0]], condition[s[1]]], input),

score = 0

for elf, condition in input:
    match (condition):
        case 0:
            score += 3 + elf
        case 1:
            move = (elf + 2)
            score += (move if move <= 3 else move - 3)
        case _:
            move = (elf + 1)
            score += 6 + (move if move <= 3 else move - 3)

print(score)
