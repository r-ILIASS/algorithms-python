from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(x=1, y=2)
p2 = Point(y=2, x=1)

print(p1 == p2)  # > True
