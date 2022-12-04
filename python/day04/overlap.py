with open('input') as inputFile:
  pairs = [line.strip().split(',') for line in inputFile]

containsAll = 0

def expand(task):
  lower, upper = task.split('-')
  return set(range(int(lower), int(upper) + 1))

for left, right in pairs:
  left = expand(left)
  right = expand(right)
  if not (left - right) or not (right - left):
    containsAll += 1

print(containsAll)

overlaps = 0
for left, right in pairs:
  left = expand(left)
  right = expand(right)
  if right & left:
    overlaps += 1
print(overlaps)
