with open('../input.txt') as inp:
    text = inp.read()
    translation = text.maketrans("ABCXYZ", "123123")

    text_split = text.translate(translation).split('\n')
    print(text_split)

    winners = {'2': '1', '3': '2', '1': '3'}
    score = 0
    for i in text_split:
        score += int(i[2])
        if i[0] == i[2]:
            score += 3
        elif winners[i[2]] == i[0]:
            score += 6

    print(score)
