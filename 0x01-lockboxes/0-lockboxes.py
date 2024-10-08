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
    visited = set()

    # Use a queue for BFS traversal
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        if current_box not in visited:
            visited.add(current_box)
            # Check the keys in the current box
            for key in boxes[current_box]:
                if key < n and not unlocked[key]:
                    queue.append(key)

    return all(unlocked)