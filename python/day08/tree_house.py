with open('input') as inputFile:
  yard = [line.strip() for line in inputFile]

visibleTrees = 0
height = len(yard)
width = len(yard[0])

for row in range(height):
  for col in range(width):
    tree = int(yard[row][col])
    for up in range(row):
      if int(yard[row - up - 1][col]) >= tree:
        break
    else:
      visibleTrees += 1
      continue
    for down in range(height - row - 1):
      if int(yard[row + down + 1][col]) >= tree:
        break
    else:
      visibleTrees += 1
      continue
    for left in range(col):
      if int(yard[row][col - left - 1]) >= tree:
        break
    else:
      visibleTrees += 1
      continue
    for right in range(width - col - 1):
      if int(yard[row][col + right + 1]) >= tree:
        break
    else:
      visibleTrees += 1
      continue

print(visibleTrees)

scenic = 0

for row in range(height):
  for col in range(width):
    tree = int(yard[row][col])
    treesUp = 0
    for up in range(row):
      treesUp += 1
      if int(yard[row - up - 1][col]) >= tree:
        break
    treesDown = 0
    for down in range(height - row - 1):
      treesDown += 1
      if int(yard[row + down + 1][col]) >= tree:
        break
    treesLeft = 0
    for left in range(col):
      treesLeft += 1
      if int(yard[row][col - left - 1]) >= tree:
        break
    treesRight = 0
    for right in range(width - col - 1):
      treesRight += 1
      if int(yard[row][col + right + 1]) >= tree:
        break
    scenic = max(scenic, treesUp * treesDown * treesLeft * treesRight)

print(scenic)
