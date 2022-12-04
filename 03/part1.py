input = open('input.txt').readlines()
input = map(lambda s: s.replace('\n', ''), input)

priorities = 0

for sack in input:
    compartments = set(sack[:len(sack)//2]), sack[len(sack)//2:]
    common = compartments[0].intersection(compartments[1])
    common = *map(lambda n: ord(n) - 64 - 26 - 6 if ord(n)
                  >= 97 else ord(n) - 64 + 26, common),
    priorities += sum(common)

print(priorities)
