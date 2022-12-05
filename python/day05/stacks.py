from collections import defaultdict
import re

stacks = defaultdict(list)
movePattern = re.compile(r'^move (\d+) from (\d+) to (\d+)')
commands = []

with open('input') as inputFile:
  for line in inputFile:
    if line[1] == '1':
      break
    for i in range(9):
      item = line[i*4+1]
      if item != ' ':
        stacks[i].append(item)
  next(inputFile)
  for line in inputFile:
    commands.append([int(a) for a in movePattern.match(line).groups()])

stacks2 = {key: list(stack) for key, stack in stacks.items()}

for no, fr, to in commands:
  for i in range(no):
    stacks[to-1].insert(0, stacks[fr-1].pop(0))

print(''.join(stacks[i][0] for i in range(9)))

for no, fr, to in commands:
  for i in range(no, 0, -1):
    stacks2[to-1].insert(0, stacks2[fr-1].pop(i-1))

print(''.join(stacks2[i][0] for i in range(9)))
