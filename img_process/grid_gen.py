def grid_gen():
    """
    Generate a non-scaled, non-translated grid of a half hexagon shape consisting of 30 points. 
    Grid places the topmost, leftmost grid point at 0,0. 
    """
    points = []
    y_scale = 1
    x_scale = 0.866025 # Triangles!
    for i in range(4, 9):
        x = (i - 4) * x_scale
        y_start = (i - 4) * y_scale * 0.5
        for j in range(i):
            y = y_start - (j * y_scale)
            points.append([x,y])
    return points

def reflect_y(pt, axis):
    """
    Reflect the x value of pt about the given x-value
    """
    delta = pt[0] - axis
    new_x = pt[0] - 2 * delta
    return [new_x, pt[1]]

if __name__ == "__main__": 
    from matplotlib import pyplot as pl

    pts = grid_gen()
    refl_pts = list([reflect_y(x, 4) for x in pts])
    pts = pts + refl_pts
    args = zip(*pts)
    pl.scatter(*args)
    pl.show()
