def max_depth(boxes):
    boxes.sort(key=sort_key, reverse=True)
    maxes = [1] * len(boxes)
    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            if boxes[i].l > boxes[j].l and boxes[i].w > boxes[j].w and boxes[i].h > boxes[j].h:
                maxes[j] = max(maxes[i] + 1, maxes[j])
    return max(maxes)

def sort_key(box):
    return box.l

# https://www.programiz.com/python-programming/methods/list/sort
# I consulted this website to learn how to sort lists of objects.