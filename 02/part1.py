input = open('input.txt').readlines()
input = *map(lambda s: s.replace('\n', '').split(' '), input),

choices = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
input = *map(lambda s: [choices[s[0]], choices[s[1]]], input),

score = 0

for elf, player in input:
    match ((elf - player) % 3):
        case 2:
            score += player + 6
        case 1:
            score += player
        case _:
            score += player + 3

print(score)
