def solution(lines):
    result = 0
    for line in lines:
        line = line.strip()
        sorted_line = sorted(line, reverse=True)

        if sorted_line[0] == line[-1] and sorted_line[0] != sorted_line[1]:
            highest = sorted_line[1]
        else:
            highest = sorted_line[0]

        pos = line.find(highest)

        second = sorted(line[pos + 1:], reverse=True)[0]
        result += int(highest + second)
    return result


if __name__ == "__main__":
    with open("../input.txt") as file:
        lines = file.readlines()

    print(solution(lines))
