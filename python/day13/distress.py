with open('input') as inputFile:
  pairs = [pair.strip().split('\n') for pair in inputFile.read().strip().split('\n\n')]
  pairs = [(eval(p[0]), eval(p[1])) for p in pairs]

def compare(left, right):
  if type(left) is int and type(right) is int:
    if left == right: return 0
    if left < right: return -1
    return 1
  if type(left) is int:
    left = [left]
  if type(right) is int:
    right = [right]
  for i, l in enumerate(left):
    if i >= len(right):
      return 1
    order = compare(l, right[i])
    if order == 0:
      continue
    return order
  if len(left) == len(right):
    return 0
  return -1

print(sum([i+1 for i, pair in enumerate(pairs) if compare(pair[0], pair[1]) == -1]))

from functools import cmp_to_key

d1, d2 = [[2]], [[6]]
packets = [packet for pair in pairs for packet in pair] + [d1, d2]
packets = sorted(packets, key=cmp_to_key(compare))
print((packets.index(d1) + 1) * (packets.index(d2) + 1))
