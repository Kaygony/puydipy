def collision(p1, p2, l):
    if p1.x >= p2.x and p1.x <= p2.x + l:
        if p1.y >= p2.y and p1.y <= p2.y + l:
            return True
    return False
