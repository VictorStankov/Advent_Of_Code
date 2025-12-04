def solution(lines, battery_num: int):
    result = 0
    for line in lines:
        line = line.strip()
        line_len = len(line)
        start_pos = 0
        batteries_left = battery_num
        num = ''

        while batteries_left > 0:
            highest = sorted(line[start_pos: line_len - batteries_left + 1], reverse=True)[0]
            start_pos = line[start_pos:line_len - batteries_left + 1].find(highest) + 1 + start_pos

            batteries_left -= 1

            num += highest
        result += int(num)

    return result


if __name__ == "__main__":
    with open("../input.txt") as file:
        lines = file.readlines()

    print(solution(lines, 12))
