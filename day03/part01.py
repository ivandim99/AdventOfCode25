with open("input.txt") as file:
    banks = [line.strip() for line in file]

total = 0
for bank in banks:
    string = str(bank)
    firstDigit = int(max(string[:-1]))
    secondDigit = int(max(string[string.find(str(firstDigit)) + 1 :]))
    total += firstDigit * 10 + secondDigit

print(total)
