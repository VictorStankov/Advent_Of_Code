with open('../input.txt') as inp:
    text_split = [''] + inp.readlines()
    helpers = []
    for i in range(len(text_split)):
        if text_split[i] == '':
            helpers.append(0)
        else:
            helpers[-1] += int(text_split[i])

    print(sorted(helpers))
    print(max(helpers))
    print(sum(sorted(helpers)[-3:]))
