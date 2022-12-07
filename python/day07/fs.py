from collections import defaultdict

sizes = defaultdict(int)
subDirs = defaultdict(set)

currentDirs = []

with open('input') as inputFile:
  for line in inputFile:
    line = line.strip()
    if line.startswith('$ cd /'):
      currentDirs = ['/']
    elif line.startswith('$ cd ..'):
      currentDirs.pop()
    elif line.startswith('$ cd'):
      currentDirs.append('/'.join(currentDirs + [line[5:]]))
    elif line == '$ ls':
      continue
    elif line.startswith('dir'):
      for dirr in currentDirs:
        subDirs[dirr].add('/'.join(currentDirs + [line[4:]]))
    else:
      num, name = line.split()
      for dirr in currentDirs:
        sizes[dirr] += int(num)

print(sum(size for size in sizes.values() if size <= 100000))

neededSpace = 30000000 - (70000000 - sizes['/'])
print(min(size for size in sizes.values() if size >= neededSpace))
