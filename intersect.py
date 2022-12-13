def intersect_rect(r1, r2):
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2
    return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)


def intersect_circle(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    return abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 > (r1 + r2) ** 2


if __name__ == "__main__":
    x1, y1, w1, h1 = map(int, input().split())
    x2, y2, w2, h2 = map(int, input().split())
    print(intersect_rect((x1, y1, w1, h1), (x2, y2, w2, h2)))
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    print(intersect_circle((x1, y1, r1), (x2, y2, r2)))
