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
    start = (start + turn) % 100
    if(start == 0):
        counter += 1

print(counter)