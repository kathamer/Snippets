"""
CheckIfSorted
Check if a list is sorted
By Dylan Hamer
"""

def sorted(checkList):
    """Check if list is sorted"""
    sorted = True
    for index, item in enumerate(checkList[:-1]):
    if not item < checkList[index+1]:
        sorted = False
    return sorted
