grid = [line.strip() for line in open("input.txt")]
R = len(grid)
C = len(grid[0])

count = 0

for r in range(R):
    for c in range(C):
        if grid[r][c] != '@':
            continue

        adj = 0
        for rr in range(r-1, r+2):
            for cc in range(c-1, c+2):
                if rr == r and cc == c:
                    continue
                if 0 <= rr < R and 0 <= cc < C:
                    if grid[rr][cc] == '@':
                        adj += 1

        if adj < 4:
            count += 1

print(count)
