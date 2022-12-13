import sys

with open('input') as inputFile:
  grid = [l.strip() for l in inputFile.read().strip().split('\n')]

S = (0, 0)
for yi, y in enumerate(grid):
  for xi, x in enumerate(y):
    if x == 'S':
      S = (xi, yi)

paths = []

DIRECTIONS = {
  'U': (0, 1),
  'D': (0, -1),
  'R': (1, 0),
  'L': (-1, 0)
}

minSteps = sys.maxsize

def walk(currPos, currChar, steps, visited):
  for direction in DIRECTIONS.values():
    x, y = currPos[0] + direction[0], currPos[1] + direction[1]
    if (x, y) in visited:
      continue
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
      continue
    newChar = grid[y][x]
    if ord('z' if newChar == 'E' else newChar) - ord(currChar) > 1:
      continue
    if newChar == 'E':
      global minSteps
      minSteps = min(minSteps, steps)
      continue
    newVisited = set(visited)
    newVisited.add((x, y))
    walk((x, y), newChar, steps + 1, newVisited)

# it does work in principle, is too slow for the big input, however :(
#walk(S, 'a', 1, {S})
#print(minSteps)

# Should do breadth-first:

from collections import deque


grid = [list(row) for row in grid]
grid[S[1]][S[0]] = 'a'

q = deque()
q.append((0, S))
visited = {S}

while q:
  steps, currPos = q.popleft()
  for direction in DIRECTIONS.values():
    x, y = currPos[0] + direction[0], currPos[1] + direction[1]
    if (x, y) in visited:
      continue
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
      continue
    currChar = grid[currPos[1]][currPos[0]]
    newChar = grid[y][x]
    if ord('z' if newChar == 'E' else newChar) - ord(currChar) > 1:
      continue
    if newChar == 'E':
      print(steps + 1)
      break
    visited.add((x, y))
    q.append((steps + 1, (x, y)))


# -- part 2

S = (0, 0)
for yi, y in enumerate(grid):
  for xi, x in enumerate(y):
    if x == 'E':
      S = (xi, yi)
grid[S[1]][S[0]] = 'z'

q = deque()
q.append((0, S))
visited = {S}

while q:
  steps, currPos = q.popleft()
  for direction in DIRECTIONS.values():
    x, y = currPos[0] + direction[0], currPos[1] + direction[1]
    if (x, y) in visited:
      continue
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
      continue
    currChar = grid[currPos[1]][currPos[0]]
    newChar = grid[y][x]
    if ord(newChar) - ord(currChar) < -1:
      continue
    if newChar == 'a':
      print(steps + 1)
      q.clear()
      break
    visited.add((x, y))
    q.append((steps + 1, (x, y)))
