from math import prod

operator_map = {
    '+': sum,
    '*': prod,
}


def solution(data):
    items_in_col = len(data) - 1

    result = 0
    nums = []

    for i in range(len(data[0]) - 1, -1, -1):
        num = ''
        for j in range(items_in_col):
            num += data[j][i]

        if not num.strip():
            continue

        nums.append(int(num))

        operator = data[items_in_col][i]
        if operator.strip():
            result += operator_map[operator](nums)
            nums.clear()

    return result


if __name__ == '__main__':
    with open('../input.txt', 'r') as file:
        data = [line.strip('\n') for line in file.readlines()]
    print(solution(data))
