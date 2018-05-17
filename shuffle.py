"""
Shuffle
Randomise the order of an array
By Dylan Hamer
"""

def shuffle(array):
"""Randomise the order of the array"""
  originalArray = array[:]
  shuffledArray = []
  for item in array:
    randomIndex = random.randint(0, len(originalArray)-1)
    shuffledArray.append(originalArray.pop(randomIndex))
  return shuffledArray
