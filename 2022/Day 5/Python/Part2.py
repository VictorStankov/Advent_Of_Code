a = {str(x): [] for x in range(1, 10)}

with open('../input.txt') as inp:
    text = inp.readlines()
    stacks, instructions = text[:8], text[10:]
    for line in stacks[::-1]:
        for i in range(9):
            if line[1 + i * 4] != ' ':
                a[str(i + 1)].append(line[1 + i * 4])

    for line in instructions:
        instruction = line.split()[1::2]
        a[instruction[2]] = a[instruction[2]] + a[instruction[1]][-int(instruction[0]):]
        a[instruction[1]] = a[instruction[1]][:-int(instruction[0])]

    for top in a.values():
        print(top[-1], end='')
