def solution(ranges):
    all_pairs = []
    result = 0

    for item_range in ranges:
        pair = item_range.split('-')
        all_pairs.append((int(pair[0]), int(pair[1])))

    all_pairs.sort(key=lambda item: item[0])
    indexes_to_skip = []

    for i in range(len(all_pairs)):
        for j in range(i + 1, len(all_pairs)):
            if i in indexes_to_skip or j in indexes_to_skip:
                continue

            pair_i = all_pairs[i]
            pair_j = all_pairs[j]

            if pair_i[1] >= pair_j[0] >= pair_i[0]:
                all_pairs[i] = (pair_i[0], max(pair_i[1], pair_j[1]))
                indexes_to_skip.append(j)

        if i not in indexes_to_skip:
            result += len(range(all_pairs[i][0], all_pairs[i][1] + 1))

    return result


if __name__ == '__main__':
    with open('../input.txt') as file:
        lines = file.readlines()
        cutoff_point = lines.index('\n')

        ranges = lines[:cutoff_point]

    print(solution(ranges))
