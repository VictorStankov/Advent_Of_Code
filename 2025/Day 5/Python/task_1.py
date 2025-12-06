def solution(ranges, items):
    all_pairs = []
    result = 0

    for item_range in ranges:
        pair = item_range.split('-')
        all_pairs.append((int(pair[0]), int(pair[1])))

    for item in items:
        for pair in all_pairs:
            if pair[0] <= int(item) <= pair[1]:
                result += 1
                break

    return result


if __name__ == '__main__':
    with open('../input.txt') as file:
        lines = file.readlines()
        cutoff_point = lines.index('\n')

        ranges = lines[:cutoff_point]
        items = lines[cutoff_point + 1:]

    print(solution(ranges, items))
