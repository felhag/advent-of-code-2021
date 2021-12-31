input = '''4738615556
6744423741
2812868827
8844365624
4546674266
4518674278
7457237431
4524873247
3153341314
3721414667'''

grid = [[int(col) for col in row] for row in input.splitlines()]
max_row = len(grid) - 1
max_col = len(grid[0]) - 1
max_flashes = 100
total_flashes = 0


def flash(row, col, flashed, increase):
    if not 0 <= row <= max_row or not 0 <= col <= max_col:
        return

    if increase:
        grid[row][col] = grid[row][col] + 1

    value = grid[row][col]
    if value <= 9 or [row, col] in flashed:
        return

    flashed.append([row, col])

    for r in range(-1, 2):
        for c in range(-1, 2):
            flash(row + r, col + c, flashed, True)


for step in range(1, 1000):
    # increase energy
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            grid[row_idx][col_idx] = grid[row_idx][col_idx] + 1

    flashed = []

    # flash
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            flash(row_idx, col_idx, flashed, False)

    # reset
    for f in flashed:
        grid[f[0]][f[1]] = 0

    print(len(flashed))
    total_flashes = total_flashes + len(flashed)

    if max_flashes == len(flashed):
        print(f'Step {step}')
        break

print(f'Total flashes: {total_flashes}')
