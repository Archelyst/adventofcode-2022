import sys

with open('input') as inputFile:
  paths = [
    [list(map(int, coord.split(','))) for coord in path.strip().split(' -> ')]
    for path in inputFile
  ]

maxX, maxY = 0, 0
for x, y in (c for coord in paths for c in coord):
  maxX, maxY = max(maxX, x), max(maxY, y)
grid = [[None for _ in range(maxX + 100)] for _ in range(maxY + 2)]

def sign(a, b):
  return (a - b) // abs(a - b) if a != b else 1

for path in paths:
  for (sx, sy), (fx, fy) in zip(path, path[1:]):
    sx, fx = sorted((sx, fx))
    sy, fy = sorted((sy, fy))
    for x in range(sx, fx + 1):
      for y in range(sy, fy + 1):
        grid[y][x] = '#'

def printGrid():
  for y in range(len(grid)):
    for x in range(450, len(grid[y])):
      print(end=grid[y][x] or '.')
    print()

def part1():
  for unit in range(sys.maxsize):
    x, y = [500, 0]
    while True:
      if y >= maxY:
        # printGrid()
        print(unit)
        return
      if grid[y+1][x] == None:
        y += 1
        continue
      if grid[y+1][x-1] == None:
        x, y = x-1, y+1
        continue
      if grid[y+1][x+1] == None:
        x, y = x+1, y+1
        continue
      grid[y][x] = 'o'
      break

part1()

# part 2

grid = [[None for _ in range(maxX + 100)] for _ in range(maxY + 3)]

for path in paths:
  for (sx, sy), (fx, fy) in zip(path, path[1:]):
    sx, fx = sorted((sx, fx))
    sy, fy = sorted((sy, fy))
    for x in range(sx, fx + 1):
      for y in range(sy, fy + 1):
        grid[y][x] = '#'


def part2():
  for unit in range(sys.maxsize):
    x, y = [500, 0]
    while True:
      if y + 1 == maxY + 2:
        grid[y][x] = 'o'
        break
      if grid[y+1][x] == None:
        y += 1
        continue
      if grid[y+1][x-1] == None:
        x, y = x-1, y+1
        continue
      if grid[y+1][x+1] == None:
        x, y = x+1, y+1
        continue
      grid[y][x] = 'o'
      if y == 0:
        print(unit + 1)
        return
      break

part2()
