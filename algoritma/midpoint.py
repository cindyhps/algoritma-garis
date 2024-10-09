def midpoint(x1, y1, x2, y2):
    points = []
    iter_steps = []
    iter_count = 0

    dx = x2 - x1
    dy = y2 - y1
    d = dy - (dx / 2)
    y = y1

    for x in range(x1, x2 + 1):
        points.append((x, y))
        iter_steps.append((iter_count, x, y))
        iter_count += 1

        if d > 0:
            y += 1
            d -= dx
        d += dy

    return points, iter_count, iter_steps
