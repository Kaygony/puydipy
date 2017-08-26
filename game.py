def collision(x1, y1, x2, y2, l):
    if x1 >= x2 and x1 <= x2 + l:
        if y1 >= y2 and y1 <= y2 + l:
            return True
    return False
