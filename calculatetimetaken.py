"""
CalculateTimeTaken
Calculate minutes, seconds and hours between two epoch points
By Dylan Hamer
"""

def calculateTimeTaken(startTime, endTime):
    """Calculate difference between two epoch points in human readable time"""
    epochTaken = endTime - startTime
    timeStructure = time.localtime(epochTaken)
    hours, minutes, seconds = timeStructure.tm_hour, timeStructure.tm_min, timeStructure.tm_sec
    print("{} {} {}".format(hours,minutes,seconds))
    return hours, minutes, seconds
