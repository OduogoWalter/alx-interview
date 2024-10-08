#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of lists): A list containing lists of keys for each box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]
    index = 0

    while index < n:
        if unlocked[index]:
            for key in keys:
                if key < n and not unlocked[key]:
                    unlocked[key] = True
            keys = keys + boxes[index]
        index += 1

    return all(unlocked)
