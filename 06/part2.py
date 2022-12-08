input = open('input.txt').readline().strip()

for i in range(12, len(input)):
    if (len(set(input[i-14:i])) == 14):
        print(i)
        break
