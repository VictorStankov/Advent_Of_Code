from math import floor, ceil

with open('../input.txt', 'r') as file:
    lines = file.readlines()

i = 50
result = 0

for line in lines:
    direction = line[0]
    number = int(line[1:])
    prev_i = i
    i = i + number * (1 if direction == 'R' else -1)

    # Handle cases when the dial is turned more than 99
    if i > 99:
        result += floor(i / 100)
        i = i % 100
        continue

    # Handle cases when the dial is turned more than 0
    if i < 0:
        result += ceil(-i / 100)

        # If we started from the 0, subtract 1 from the result to correct the count
        if prev_i == 0:
            result -= 1

        i += ceil(-i / 100) * 100

    if i == 0:
        result += 1

print(result)