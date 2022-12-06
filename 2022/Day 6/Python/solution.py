def find(search_text: str, num_char: int) -> int:
    for i in range(len(search_text) - num_char):
        if len(set(search_text[i:i + num_char])) == num_char:
            return i + num_char


with open('../input.txt') as inp:
    text = inp.read()
    print(find(text, 4), find(text, 14))
