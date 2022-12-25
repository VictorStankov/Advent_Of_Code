import matplotlib.pyplot as plt
import numpy as np
from drawnow import drawnow

from point import Point

coord = {(0, 0)}
points = [Point() for _ in range(10)]
x, y = 0, 0


def print_points():
    global points, x, y  # points is imported like this, because the drawnow doesn't pass any arguments >:(
    # As for x and y, Python doesn't have static function variables 2x >:(

    vals: list[tuple] = list(zip(*[j.vals() for j in points] + [(x, y)]))
    x, y = (max(map(abs, vals[0]))), (max(map(abs, vals[1])))
    matrix = np.zeros(((y + 10) * 2, (x + 10) * 2))
    for point in coord:
        matrix[point[1] + (matrix.shape[0] // 2)][point[0] + (matrix.shape[1] // 2)] = 5
    for k in range(len(points)):
        matrix[points[k].y + matrix.shape[0] // 2][points[k].x + matrix.shape[1] // 2] = k + 10
    plt.imshow(matrix)


with open('../input.txt') as inp:
    text = [x.split(' ') for x in inp.read().splitlines()]
    for bearing, value in text:
        mod = 1 if bearing in 'RD' else -1
        for _ in range(int(value)):
            if bearing in 'UD':
                points[0].move_y(1 * mod)
            else:
                points[0].move_x(1 * mod)
            value = int(value) - 1

            for i in range(1, len(points)):
                diff = points[i - 1] - points[i]
                while max(map(abs, points[i - 1] - points[i])) > 1:
                    diff = points[i - 1] - points[i]
                    points[i].move_x(0 if diff[0] == 0 else diff[0] // abs(diff[0]))
                    points[i].move_y(0 if diff[1] == 0 else diff[1] // abs(diff[1]))
                    drawnow(print_points)  # Very slow, disable for results
                    if i == 9:  # Which element to be checked: Part 1: 1, Part 2: 9
                        coord.add((points[i].x, points[i].y))

print(len(coord))
