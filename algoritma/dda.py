def dda(x1, y1, x2, y2):
    points = []
    iter_steps = []
    iter_count = 0

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x, y = x1, y1
    for i in range(steps + 1):
        points.append((round(x), round(y)))
        iter_steps.append((iter_count, round(x), round(y)))
        x += x_increment
        y += y_increment
        iter_count += 1

    return points, iter_count, iter_steps
