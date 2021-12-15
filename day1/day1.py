def readFile(filePath):
  lines = []
  with open(filePath) as f:
    lines = f.readlines()
  return lines

def day1(offset):
  increasedCount = 0
  lines = readFile("./day1-data.txt")

  for i, num in enumerate(lines):
    if i < offset: continue
    if int(num) > int(lines[i-offset]): increasedCount += 1
  
  return increasedCount

print(f"part 1: {day1(1)}")
print(f"part 12: {day1(3)}")