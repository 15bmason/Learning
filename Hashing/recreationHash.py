def changeTo8Bit(x):
    temp = x.split()
    temp1= []
    for i in temp:
        temp1.append("0"*(8-len(i)) + i)    
    return temp1

def backToString(x):
    temp = ""
    for i in range(len(x)):
        if i != len(x) - 1:
            temp += (x[i] + " ")
        else:
            temp += (x[i])
    return temp

def calcBigEndian(x):
    temp = bin(x * 8)
    return " 00000000"*7 + " " + backToString(changeTo8Bit(temp[2:]))

initialStr = input("Enter a string: ")
initialLen = len(initialStr)
print(initialLen)
initialStr = ' '.join(format(ord(x), 'b') for x in initialStr)

initialStr = changeTo8Bit(initialStr)

initialStr = backToString(initialStr)

for i in range(int(448/8) - initialLen):
    if i != 0:
        initialStr += " 00000000"
    else: 
        initialStr += " 10000000"
    
initialStr += calcBigEndian(initialLen)

print(initialStr)

#h0 = 0x6a09e667
#h1 = 0xbb67ae85
#h2 = 0x3c6ef372
#h3 = 0xa54ff53a
#h4 = 0x510e527f
#h5 = 0x9b05688c
#h6 = 0x1f83d9ab
#h7 = 0x5be0cd19
