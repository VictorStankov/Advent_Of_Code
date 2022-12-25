import numpy as np

c = 0
max_result = 0
f = np.genfromtxt('../input.txt', delimiter=1, dtype=int)
for i in range(1, f.shape[0] - 1):
    for j in range(1, f.shape[0] - 1):
        if any(x < f[i, j] for x in (max(f[:i, j]), max(f[i+1:, j]), max(f[i, :j]), max(f[i, j+1:]))):
            c += 1

        horiz = np.where(f[i] >= f[i, j])[0]
        vert = np.where(f[:, j] >= f[i, j])[0]
        horiz_ind, vert_ind = horiz.searchsorted(j), vert.searchsorted(i)
        horiz_split, vert_split = np.split(horiz, [horiz_ind, horiz_ind+1]), np.split(vert, [vert_ind, vert_ind+1])
        result = (j - (np.insert(horiz_split[0], 0, 0))[-1]) * ((np.append(horiz_split[2], 98))[0] - j) * \
                 (i - (np.insert(vert_split[0], 0, 0))[-1]) * ((np.append(vert_split[2], 98))[0] - i)
        if result > max_result:
            max_result = result

print(c + (f.shape[0] + f.shape[1]) * 2 - 4)
print(max_result)
