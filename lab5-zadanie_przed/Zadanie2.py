
def distance_one_dimension(size, p1, p2):
    if (abs(p1) > size or abs(p2) > size):
        raise IndexError
    if ((p1 >= 0 and p2 >= 0) or (p1 <= 0 and p2 <= 0) or (abs(p1) < size / 2 and abs(p2) < size/2)):
        return abs(p1 - p2)
    else:
        if (p1 > 0 and p2 < 0):
            p1 = -p1
        if (p2 > 0 and p1 < 0):
            p2 = -p2
        return abs(p1 % size+p2 % size + 1)


def distance(size, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return distance_one_dimension(size, x1, x2) + distance_one_dimension(size, y1, y2)
