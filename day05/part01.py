ranges, numbers = open("input.txt").read().split("\n\n")

ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
numbers = list(map(int, numbers.splitlines()))

count = 0

for num in numbers:
    for low, high in ranges:
        if low <= num <= high:
            count += 1
            break

print(count)