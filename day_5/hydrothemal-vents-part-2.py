import numpy as np

with open("input.txt") as f:
    coordinates = []
    for line in f.readlines():
        coordinates.append(list(map(int ,line.replace("->", ",").replace("\n", "").split(","))))

    coordinates_array = np.array(coordinates, dtype=int)

grid_size = 1000

Y, X = np.indices((grid_size, grid_size))
linear_space = np.linspace(0, grid_size, num=grid_size, dtype=int)

# You don't need to do this (at all, look at sparse matrices), did this for visualisation. Will optimise afterwards.

def xy_to_grid(x, y):
    grid = np.array(np.where(X == x, 1, 0) + np.where(Y == y, 1, 0) == 2, dtype=int)
    return grid

def generate_coordinates(x1, y1, x2, y2):
    generate_points = {(x1, y1), (x2, y2)}
    match = False

    if x1 == x2:
        for i in range(abs(y2 - y1)):
            if y2 > y1:
                generate_points.add((x1, y1 + i))
            else:
                generate_points.add((x2, y2 + i))
        match = True
    elif y1 == y2:
        for i in range(abs(x2 - x1)):
            if x2 > x1:
                generate_points.add((x1 + i, y1))
            else:
                generate_points.add((x2 + i, y2))
        match = True

    elif abs((x1 - x2)/(y1 - y2)) == 1:
        m = (x1 - x2)//(y1 - y2)
        b = -1*x1*m + y1
        x = linear_space
        y = m*x + b

        diagonal_line = list(map(tuple, zip(x, y)))

        start = diagonal_line.index((x1, y1))
        end = diagonal_line.index((x2, y2))

        if start > end:
            start, end = end, start

        for coordinate in diagonal_line[start:end]:
            generate_points.add(coordinate)

        match = True

    return generate_points, match

imputed_grid = np.zeros((grid_size, grid_size), dtype=int)
print_grid = True

for coordinate_number, coordinate in enumerate(coordinates_array):

    x1, y1, x2, y2 = coordinate

    generated_coordinates, match = generate_coordinates(x1, y1, x2, y2)

    if print_grid:

        if match:
            for point in generated_coordinates:
                x,y = point
                imputed_grid += xy_to_grid(x, y)

    progress = (coordinate_number+1)/coordinates_array.shape[0]
    print(f"Progress: {round(progress*100,2)}%")

print(len(imputed_grid[imputed_grid >= 2])) # 20271