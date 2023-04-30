import random
name=[]#定义一个空列表
namelist=["小张","小王","小李"]
textlist=[1,"测试"] #列表中可以存储混合类型
#查【in ，not in】
'''
findname=input("查找姓名")
if findname in namelist:
    print("有")
else:
    print("没有找到")
'''
mylist =["a","b","c","a","b"]
'''
print(mylist.index("a",1,4))#可以查找指定下标范围的元素，并返回找回对应数据的下标
print(mylist.index("a",1,3))#范围区间，左闭右开【1，3）
                            #找不到会报错

print(mylist.count("c")) #统计某个元素出现了几次
'''
#排序和反转
'''
a=[1,4,2,3]
print(a)
a.reverse()#将列表所以元素反转
print(a)
a.sort(reverse=True)#默认排序升序，现在降序
print(a)
'''
#schollname=[[],[],[]]  #有三个元素的空列表，每个元素都是一个空列表
schollname=[["北京大学","清华大学"],["南开大学","天津大学"]]
print(schollname[0][0])

offices=[[],[],[]]
names=["a","b","v","c","d"]
for name in names:
    index=random.randint(0,2)
    offices[index].append(name)
i=1
for office in offices:
    print("办公室%d人数：%d"%(i,len(office)))
    i+=1
    for name in office:
        print("%s"%name,end="\t")
    print("\n")
    print("-"*20)




