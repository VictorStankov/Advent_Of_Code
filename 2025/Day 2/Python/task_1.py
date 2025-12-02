from math import floor

with open('../input.txt', 'r') as file:
    line = file.readline()

result = 0

for code_pair in line.split(','):
    start, end = code_pair.split('-')
    for i in range(int(start), int(end) + 1):
        string_to_check = str(i)
        half_length = floor(len(string_to_check) / 2)
        if string_to_check[:half_length] == string_to_check[half_length:]:
            result += i

print(result)