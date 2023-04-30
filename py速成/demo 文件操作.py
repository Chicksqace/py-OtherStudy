# f=open("test.txt","w")   #打开文件,W模式（写模式），文件不存在就新建
# f.write("hellohhhhhhhwdado") #将字符串写入文件中
#
#
#
# f.close()  #关闭文件
''' #read 方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
f=open("test.txt","r")
content=f.read(5)
print(content)
content=f.read(5)
print(content)
f.close()
'''
'''
f=open("test.txt","r")
content=f.readlines() #一次性读取全部文件为列表，每行一个字符串元素
print(content)
i=1
for temp in content:
    print("第%d:%s"%(i,temp))
    i+=1
f.close()
'''
'''
f=open("test.txt","r")
content=f.readlines()
print("1:%s"%content,end="")
content=f.readline()
print("2:%s"%content)
f.close()
'''
import os
os.rename("test.txt","test1.txt")




















