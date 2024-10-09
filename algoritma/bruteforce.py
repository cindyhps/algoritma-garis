def brute_force(x1, y1, x2, y2):
    points = []
    iter_steps = []
    iter_count = 0

    dx = x2 - x1
    dy = y2 - y1

    for x in range(x1, x2 + 1):
        y = y1 + dy * (x - x1) // dx
        points.append((x, y))
        iter_steps.append((iter_count, x, y))
        iter_count += 1

    return points, iter_count, iter_steps
