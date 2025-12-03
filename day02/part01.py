with open("input.txt") as file:
    ranges = [
        [int(start),int(end)] 
        for line in file
        for part in line.strip().split(",")
        for start,end in [part.split("-")]
    ]

numbers = sum((list(range(a, b + 1)) for a, b in ranges), [])

ret = 0

for num in numbers:
    string = str(num)
    length = len(string)
    if length % 2 == 0 and string[:length//2] == string[length//2:]:
        ret += num

print (ret)