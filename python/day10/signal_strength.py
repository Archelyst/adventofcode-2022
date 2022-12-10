with open('input') as inputFile:
  operations = [line.strip().split() for line in inputFile]

cycles = []
for op in operations:
  if op[0] == 'noop':
    cycles.append(op)
  else:
    cycles.append(['noop'])
    cycles.append(op)

X = 1
sigSum = 0

for no, cycle in enumerate(cycles, 1):
  if ((no + 20) % 40 == 0):
    sigSum += no * X
  if no > 220:
    break
  if cycle[0] == 'addx':
    X += int(cycle[1])

print(sigSum)


# ---- part 2

X = 1
cursor = 0

for cycle in cycles:
  print('#' if cursor in (X-1, X, X+1) else '.', end='')
  cursor += 1
  if cursor == 40:
    print('')
    cursor = 0
  if cycle[0] == 'addx':
    X += int(cycle[1])
