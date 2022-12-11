import re
from dataclasses import dataclass
from copy import deepcopy
from collections import deque

patt = re.compile(r"""Monkey (\d+):
  Starting items: (.+)
  Operation: new = (.+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)""", re.M)

@dataclass
class Monkey:
  items: list
  op: str
  test: int
  ifTrue: int
  ifFalse: int
  actions: int = 0

monkeys = []

with open('test') as inputFile:
  for monk in inputFile.read().split('\n\n'):
    no, items, op, test, ifTrue, ifFalse = patt.match(monk).groups()
    exec('def op(old):\n  return ' + op)
    monkeys.append(Monkey(
      deque([int(item) for item in items.split(', ')]), op, int(test), int(ifTrue), int(ifFalse)
    ))

monkeys2 = [deepcopy(m) for m in monkeys]

for round in range(20):
  for monkey in monkeys:
    while monkey.items:
      monkey.actions += 1
      old = monkey.items.popleft()
      new = monkey.op(old) // 3
      target = monkey.ifTrue if new % monkey.test == 0 else monkey.ifFalse
      monkeys[target].items.append(new)

mostActive = sorted([monkey.actions for monkey in monkeys])[-2:]
print(mostActive[0] * mostActive[1])

# part 2 -- not completely solved on my own :(

commonDivisor = 1
for monkey in monkeys2:
  commonDivisor *= monkey.test

for round in range(10000):
  for monkey in monkeys2:
    while monkey.items:
      monkey.actions += 1
      old = monkey.items.popleft()
      new = monkey.op(old)
      new %= commonDivisor
      target = monkey.ifTrue if new % monkey.test == 0 else monkey.ifFalse
      monkeys2[target].items.append(new)

mostActive = sorted([monkey.actions for monkey in monkeys2])[-2:]
print(mostActive[0] * mostActive[1])
