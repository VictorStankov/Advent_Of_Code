with open('../input.txt') as inp:
    text = inp.read()
    translation = text.maketrans("ABC", "123")

    text_split = text.translate(translation).split('\n')

    losers = {'1': 3, '2': 1, '3': 2}
    score = 0
    for i in text_split:
        if i[2] == 'Y':
            score += 3 + int(i[0])
        elif i[2] == 'Z':
            score += 6 + int(i[0]) % 3 + 1
        else:
            score += losers[i[0]]

    print(score)
