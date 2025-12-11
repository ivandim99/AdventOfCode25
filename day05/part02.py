ranges, _ = open("input.txt").read().split("\n\n")
ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
ranges.sort()

count = 0
last = None

for low, high in ranges:
    
    if last is None:
        last = (low, high)
        
    elif last[1] < low:
        count += last[1] - last[0] + 1
        last = (low, high)
    
    else:
        last = (last[0], max(last[1], high))

count += last[1] - last[0] + 1

print(count)