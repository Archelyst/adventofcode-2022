import re

y = 2000000
sensors = []
numPatt = re.compile(r'(-?\d+)')
beaconsOnY = set()
with open('input') as inputFile:
  for line in inputFile:
    sx, sy, bx, by = map(int, numPatt.findall(line))
    sensors.append({
      'x': sx,
      'y': sy,
      'dist': abs(sx - bx) + abs(sy - by)
    })
    if by == y:
      beaconsOnY.add(bx)

covered = set()
for sensor in sensors:
  remain = sensor['dist'] - abs(sensor['y'] - y)
  if remain < 0:
    continue
  for diff in range(remain + 1):
    covered.add(sensor['x'] + diff)
    covered.add(sensor['x'] - diff)

print(len(covered - beaconsOnY))

for i, sensor in enumerate(sensors):
  for r in range(sensor['dist'] + 1):
    ydiff, xdiff = r, (sensor['dist'] + 1 - r)
    for xs, ys in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
      y = sensor['y'] + ydiff * ys
      x = sensor['x'] + xdiff * xs
      if x < 0 or y < 0 or x > 4000000 or y > 4000000:
        continue
      if all((abs(s['x'] - x) + abs(s['y'] - y)) > s['dist'] for s in sensors):
        print(sensor, x, y, x * 4000000 + y, abs(sensor['x'] - x) + abs(sensor['y'] - y))
