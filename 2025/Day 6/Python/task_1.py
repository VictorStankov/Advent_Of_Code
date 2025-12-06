import re
from math import prod

operator_map = {
    '+': sum,
    '*': prod,
}


def solution(data):
    items_in_col = len(data) - 1

    result = 0

    for i in range(len(data[0])):
        nums = []
        for j in range(0, items_in_col):
            nums.append(int(data[j][i]))
        result += operator_map[data[items_in_col][i]](nums)
    return result


if __name__ == '__main__':
    with open('../input.txt', 'r') as file:
        data = [re.sub(' +', ' ', line).strip().split(' ') for line in file.readlines()]
    print(solution(data))
