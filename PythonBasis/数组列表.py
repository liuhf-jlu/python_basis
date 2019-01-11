number = []
i = 0

while i < 10:
    number.append(i + 100) # 填充数组append
    i = i + 1

i = 0
while i < 10:
    print("number[%d] = %d" %(i,number[i]))
    i = i + 1