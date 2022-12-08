input = open('input.txt').readline().strip()

for i in range(2, len(input)):
    if (len(set(input[i-4:i])) == 4):
        print(i)
        break
