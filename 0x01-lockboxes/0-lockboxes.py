#!/usr/bin/python3

def canUnlockAll(boxes):
    opened_boxes = set([0])
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                keys.append(key)

    return len(opened_boxes) == len(boxes)
