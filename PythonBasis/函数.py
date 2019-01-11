# 求集合中的最大值
def getMax(set):
    max = set[0]
    i = 1
    while (i < 5):
        if (max < set[i]):
            max = set[i]
        i = i + 1
    return max


# 求集合中的最小值
def getMin(set):
    min = set[0]
    i = 1
    while (i < 5):
        if (min > set[i]):
            min = set[i]
        i = i + 1
    return min


set1 = [10, 20, 30, 40, 50]
set2 = [101, 201, 301, 401, 501]

max = getMax(set1)
print("Max in set1 is ", max)

min = getMin(set2)
print("Min in set2 is ", min)
