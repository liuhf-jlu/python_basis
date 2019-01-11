# 创建新文件
fo = open("/home/test/Desktop/test2.txt", "w")

# 字符串写入文件
fo.write("This is testing for python write...\n")
fo.write("This is second line...\n")

# 关闭文件
fo.close()

# 打开已经存在的文件
fo = open("/home/test/Desktop/test2.txt", "r")

# 读取文件的内容
str = fo.read(100)
print(str)

# 关闭文件
fo.close()
