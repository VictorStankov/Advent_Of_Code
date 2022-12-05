import pandas as pd

a = pd.read_csv('../input.txt', header=None)
a[[2, 3]] = a[0].str.split('-', expand=True)
a[[4, 5]] = a[1].str.split('-', expand=True)
a[[2, 3, 4, 5]] = a[[2, 3, 4, 5]].apply(pd.to_numeric)
a[6] = a[4] - a[2]
a[7] = a[3] - a[5]

counter = 0
counter2 = 0

for row in a.values:
    if (row[6] <= 0 and row[7] <= 0) or (row[6] >= 0 and row[7] >= 0):
        counter += 1
    if row[4] <= row[3] <= row[5] or row[2] <= row[5] <= row[3] or \
            row[4] <= row[3] <= row[5] or row[2] <= row[5] <= row[3]:
        counter2 += 1

print(counter, counter2)
