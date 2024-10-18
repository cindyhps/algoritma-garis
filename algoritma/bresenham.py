def bresenham(x1, y1, x2, y2):
    points = []
    iter_steps = []
    iter_count = 0

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1 #arah garis sumbu x
    sy = 1 if y1 < y2 else -1 #arah garis sumbu y
    err = dx - dy

    while True:
        points.append((x1, y1))
        iter_steps.append((iter_count, x1, y1)) #hitung iterasi
        iter_count += 1

        if x1 == x2 and y1 == y2: 
            break
        e2 = err * 2 #menghindari float point
        if e2 > -dy: 
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points, iter_count, iter_steps
