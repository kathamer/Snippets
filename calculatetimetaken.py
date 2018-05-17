"""
CalculateTimeTaken
Calculate minutes, seconds and hours between two epoch points
By Dylan Hamer
"""

import time  # Deal with time

def calculateTimeTaken(startTime, endTime):
    """Calculate difference between two epoch points in human readable time"""
    epochTaken = endTime - startTime  # Get raw difference between two floating points
    timeStructure = time.localtime(epochTaken)  # Structure a time constructor using localtime
    hours, minutes, seconds = timeStructure.tm_hour, timeStructure.tm_min, timeStructure.tm_sec  # Get hours, minutes and seconds
    return hours, minutes, seconds
