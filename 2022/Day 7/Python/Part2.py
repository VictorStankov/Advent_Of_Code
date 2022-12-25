sizes = []


class Directory:
    def __init__(self):
        self.subdirectories = {}
        self.size = 0

    def __repr__(self):
        return str(self.subdirectories) + str(self.size)

    def calc_size(self):
        global sizes
        ret_size = self.size
        for folder in self.subdirectories.values():
            ret_size += folder.calc_size()
        sizes.append(ret_size)
        return ret_size


base_dir = cur_dir = Directory()
dir_path = []

with open('../input.txt') as inp:
    text = inp.read().splitlines()
    for line in text:
        if line[:4] == '$ cd':
            if line[5:] != '..':
                dir_path.append(line[5:])
                cur_dir.subdirectories[line[5:]] = Directory()
                cur_dir = cur_dir.subdirectories[line[5:]]
            else:
                dir_path.pop()
                cur_dir = base_dir
                for el in dir_path:
                    cur_dir = cur_dir.subdirectories[el]
        elif line[0].isdigit():
            cur_dir.size += int(line.split()[0])

a = base_dir.calc_size()
free_space = 70000000 - sorted(sizes)[-1]
for i in sorted(sizes):
    if free_space + i >= 30000000:
        print(i)
        break
