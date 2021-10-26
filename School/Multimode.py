_digits = input("Entry pls: ")
digits = []
for i in _digits: digits.append(i)
temp = 0
prev = []
for i in digits:
    counter = 1
    ch = i
    for j in range(len(digits) - 1):
        if digits[j] == digits[j+1]:
            counter += 1
            if counter > temp:
                temp = counter
            else:
                prev.append(str(counter) + " " + ch)
        else:
            prev.append(str(counter) + " " + ch)
            counter = 1

print(prev)
print(temp)
