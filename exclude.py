"""
Exclude 
Exclude an item at a specified index from a list
By Dylan Hamer
"""

def exclude(originalList, exclusionIndex):
    """Return a given list without a specified element"""
    newList = originalList[:]  # Make original list not mutable
    if exclusionIndex <= len(newList): # Check if list has item
        newList.pop(exclusionIndex)  # Remove item at specific index
        return newList
    else:  # If it doesn't have the item
        raise IndexError("Could not exclude {}".format(exclusion))  # Raise an error condition
