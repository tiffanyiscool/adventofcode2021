def readFile(filePath):
  formattedData = []
  with open(filePath) as file:
    for line in file:
      lineList = line.split()
      formattedDirection = [str(lineList[0]), int(lineList[1])]
      formattedData.append(formattedDirection)
  return formattedData

# part 1
def getFinalCoordinates(directionsList):
  position = 0
  depth = 0
  for direction in directionsList:
    if direction[0] == "forward": position += direction[1]
    if direction[0] == "up": depth -= direction[1]
    if direction[0] == "down": depth += direction[1]
  return [position, depth]

# part 2
def getFinalCoordinatesWithAim(directionsList):
  position = 0
  depth = 0
  aim = 0
  for direction in directionsList:
    if direction[0] == "forward": 
      position += direction[1]
      depth += aim * direction[1]
    if direction[0] == "up": aim -= direction[1]
    if direction[0] == "down": aim += direction[1]
  return [position, depth]

def part1():
  coordinatesList = getFinalCoordinates(readFile("./day2-data.txt"))
  return coordinatesList[0] * coordinatesList[1]

def part2():
  coordinatesList = getFinalCoordinatesWithAim(readFile("./day2-data.txt"))
  return coordinatesList[0] * coordinatesList[1]

print(part1())
print(part2())
# print(getFinalCoordinates(readFile("./day2-data.txt")))