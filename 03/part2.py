input = open('input.txt').readlines()
input = map(lambda s: s.replace('\n', ''), input)

priorities = 0

for a, b, c in zip(*[iter(input)]*3):
    common = set(a).intersection(b).intersection(c)
    common = *map(lambda n: ord(n) - 64 - 26 - 6 if ord(n)
                  >= 97 else ord(n) - 64 + 26, common),
    priorities += sum(common)

print(priorities)
