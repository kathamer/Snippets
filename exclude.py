"""
Exclude 
Exclude an item at a specified index from a list
By Dylan Hamer
"""

def exclude(originalList, exclusionIndex):
    """Return a given list without a specified element"""
    newList = originalList[:]  # Make original list not mutable
    if exclusionIndex <= len(newList)  # Check if list has item
        return newList.pop(exclusion)  # Return list but without exclusion
    else:  # If it doesn't have the item
        raise IndexError("Could not exclude {}".format(exclusion))  # Raise an error condition
