prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def solution(input_line: str):
    result = 0

    for code_pair in input_line.split(','):
        start, end = code_pair.split('-')

        for num in range(int(start), int(end) + 1):
            str_num = str(num)
            length = len(str_num)

            # The idea is we check if the length of the ID is divisible by a prime number. If it is, we check whether
            # the first N characters repeated by that prime number is the same as the original string, where N is the
            # length of the string divided by the prime number
            for prime_num in prime_nums:
                if prime_num > length:
                    break

                if length % prime_num != 0:
                    continue

                if str_num[:length // prime_num] * prime_num == str_num:
                    result += num
                    break

if __name__ == '__main__':
    with open('../input.txt', 'r') as file:
        line = file.readline()

    print(solution(line))
