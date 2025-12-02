with open('../input.txt', 'r') as file:
    lines = file.readlines()

i = 50
result = 0

for line in lines:
    direction = line[0]
    number = int(line[1:])
    i = i + number * (1 if direction == 'R' else -1)

    # Handle cases when the dial is turned more than 99
    i = i % 100

    # Handle cases when the dial is turned more than 0
    if i < 0:
        i += 100

    if i == 0:
        result += 1

print(result)