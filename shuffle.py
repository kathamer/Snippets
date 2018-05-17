"""
Shuffle
Randomise the order of a list while keeping non-unique elements
By Dylan Hamer
"""

def shuffle(shuffleList):
  """Randomise the order of the array"""
  originalList = shuffleList[:]  # Make array immutable
  shuffledList = []
  for item in shuffleList:
    randomIndex = random.randint(0, len(originalList)-1)
    shuffledList.append(originalList.pop(randomIndex))
  return shuffledList
