name=[]#定义一个空列表
namelist=["小张","小王","小李"]
textlist=[1,"测试"] #列表中可以存储混合类型
# for i in range(3):
#     print(namelist[i])
# print(type(textlist[0]))
# for name in namelist:
#     print(name)
#
#
# len=len(namelist)     #可以得到列表长度
# while i <len:
#     print(namelist[i])
#     i+=1
#增 (append)
'''
print("增加前")
for name in namelist:
    print(name)
nametemp=input("请输入增加数据")
namelist.append(nametemp)   #在末尾增加一个元素

print("增加后")
for name in namelist:
    print(name)
'''
'''
a=[1,2]
b=[3,4]
a.append(b)             #将列表当做一个元素，加入a的列表
print(a)
a.extend(b)
print(a)                #将b列表中的每一个元素一一加入到a列表中
'''
#增：    [insert]插入
'''
a=[0,1,2]
a.insert(1,3)      #第一个变量表示下标,第二个表示元素(对象)
print(a)           #指定下标位置插入元素
'''
'''
#删  [del]
namelist=["fasf","gsggf","fsdfdw","qfwtrrte"]
print("删除前")
for name in namelist:
    print(name)
del namelist[2]  #在末尾删除一个元素
print("删除后")
for name in namelist:
    print(name)
'''
#删  [pop]
'''
namelist=["fasf","gsggf","fsdfdw","qfwtrrte"]
print("删除前")
for name in namelist:
    print(name)
namelist.pop()  #在末尾弹出一个元素
print("删除后")
for name in namelist:
    print(name)
'''
#remove移除
'''
namelist=["fasf","gsggf","fsdfdw","qfwtrrte","gsggf"]
print("删除前")
for name in namelist:
    print(name)
namelist.remove("gsggf")  #直接删除指定内容过的元素
print("删除后")
for name in namelist:
    print(name)
'''
#改：
print("删除前")
for name in namelist:
    print(name)
namelist[1]="小红" #修改指定下标的元素内容
print("删除后")
for name in namelist:
    print(name)

