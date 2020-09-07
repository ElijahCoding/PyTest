from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)

print(d)

d.pop()
d.popleft()

print(d)


d.extend([4,5,6])
d.extendleft([7,8,9])

d.rotate(-1)