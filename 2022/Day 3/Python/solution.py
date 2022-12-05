with open('../input.txt') as inp:
    lines = inp.read().split('\n')
    sum = 0
    sub_values = {0: 38, 1: 96}
    for line in lines:
        for i in range(len(line) // 2):
            dupl = set(line[:len(line) // 2]).intersection(line[len(line) // 2:]).pop()
            sum += ord(dupl) - sub_values[dupl.islower()]
            break
    print(sum)

    sum = 0
    for i in range(len(lines) // 3):
        badge = set(lines[i * 3]).intersection(lines[i * 3 + 1], lines[i * 3 + 2]).pop()
        sum += ord(badge) - sub_values[badge.islower()]
    print(sum)
