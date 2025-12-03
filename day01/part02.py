with open("input.txt") as file:
    steps = [line.strip() for line in file]

converted = []

for step in steps: 
    if("L" in step):
        converted.append(- int(step.strip("L")))
    else: 
        converted.append(int(step.strip("R")))

counter = 0
start = 50

for turn in converted:
    if(turn < 0):
        div = turn // -100
        mod = turn % -100
        counter += div
        if start != 0 and start + mod <= 0:
            counter += 1
    else:
        div = turn // 100
        mod = turn % 100
        counter += div
        if start + mod >= 100:
            counter += 1

    start = (start + turn) % 100

print(counter)