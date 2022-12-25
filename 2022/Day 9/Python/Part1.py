from point import Point

coord = {(0, 0)}
head, tail = Point(), Point()

with open('../input.txt') as inp:
    text = [x.split(' ') for x in inp.read().splitlines()]
    for bearing, value in text:
        mod = 1 if bearing in 'RD' else -1
        if bearing in 'UD':
            head.move(True, int(value) * mod)
        else:
            head.move(False, int(value) * mod)

        while max(map(abs, head - tail)) > 1:
            diff = head - tail
            tail.move(False, 0 if diff[0] == 0 else diff[0] // abs(diff[0]))
            tail.move(True, 0 if diff[1] == 0 else diff[1] // abs(diff[1]))
            coord.add((tail.x, tail.y))

print(len(coord))
