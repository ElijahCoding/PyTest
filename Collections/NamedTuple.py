from collections import namedtuple

Point = namedtuple('Point', 'x,y')

pt = Point(1, -4)

print(pt.x, pt.y)

Custom = namedtuple('Custom', 'a,b')
custom = Custom(5,6)
print(custom.a, custom.b)