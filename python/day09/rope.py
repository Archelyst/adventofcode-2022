with open('input') as inputFile:
  movements = [line.strip().split() for line in inputFile]

DIRECTIONS = {
  'U': (0, 1),
  'D': (0, -1),
  'R': (1, 0),
  'L': (-1, 0)
}

# ---- part 1

movements = [(DIRECTIONS[m[0]], int(m[1])) for m in movements]
visited = set()

head = (0, 0)
tail = (0, 0)
visited.add(tail)
for direction, amount in movements:
  for _ in range(amount):
    head = head[0] + direction[0], head[1] + direction[1]
    xDiff = head[0] - tail[0]
    yDiff = head[1] - tail[1]
    if abs(xDiff) > 1 or abs(yDiff) > 1:
      if abs(xDiff):
        tail = tail[0] + xDiff / abs(xDiff), tail[1]
      if abs(yDiff):
        tail = tail[0], tail[1] + yDiff / abs(yDiff)
      visited.add(tail)

print(len(visited))

# ---- part 2

knots = [(0, 0) for _ in range(10)]
visited = set()

def moveSuccessor(predecessorIndex, successorIndex):
  predecessor, successor = knots[predecessorIndex], knots[successorIndex]
  xDiff = predecessor[0] - successor[0]
  yDiff = predecessor[1] - successor[1]
  if abs(xDiff) > 1 or abs(yDiff) > 1:
    if abs(xDiff):
      successor = successor[0] + xDiff / abs(xDiff), successor[1]
    if abs(yDiff):
      successor = successor[0], successor[1] + yDiff / abs(yDiff)
  knots[successorIndex] = successor

for direction, amount in movements:
  for _ in range(amount):
    knots[0] = knots[0][0] + direction[0], knots[0][1] + direction[1]
    for i in range(1, 10):
      moveSuccessor(i-1, i)
    visited.add(knots[9])

print(len(visited))
