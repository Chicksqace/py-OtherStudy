'''
#函数的定义
def printinfo():
    print("!!!!!!!!!!!!!")
    print("人生苦短，我用python")
    print("!!!!!!!!!!!!!")
#函数的调用
printinfo()
'''
#带参数的函数
'''
def add2num(a,b):
    c=a+b
    print(c)
add2num(11,22)
'''
'''
#带返回值的函数
def add2num(a,b):
    return a+b   #通过return 返回运算结果
result=add2num(11,22)
print(result)
#print(add2num(11,22))
'''
'''
#返回多个值的函数
def divid(a,b):
    shang=a/b
    yushu=a%b
    return shang,yushu#多个返回值用逗号分隔
sh,yu=divid(5,2)  #需要多个值来返回内容
print("商:%d,余数:%d"%(sh,yu))
'''
'''
def printoneline():
    print('-'*30)
#printoneline()
#根据用户输入的数字打印相应线
def printnumline(num):
    i=0
    while i<num:
        printoneline()
        i+=1
printnumline(3)
'''
#求三个数的和
# def sum3number(a,b,c):
#     return a+b+c
# print(sum3number(10,20,30))
# #完成三个数的平均值
# def avaer(a,b,c):
#     sumresult=sum3number(10,20,30)
#     averesult=sumresult/3.0
#     return averesult
# result=avaer(10,20,30)
# print("平均值为:%d"%result)
#全局变量和局部变量
'''
def text1():
    a=300  #局部变量
    print(a)
    a=100
    print(a)
text1()
def text2():
    a=500#不同的函数定义相同名字，彼此无关
    print(a)
text2()
'''
'''
a=100 #全局变量
def text1():
    a=300#局部变量优先使用
    print(a)
    a=312
    print(a)
text1()
def text2():
    print(a)#调用全局变量a，默认使用全局变量
text2()
#全局变量和局部变量一样
'''
#在函数中修改全局变量

a=100 #全局变量
def text1():
    global a#声明全局变量在函数中的标识符
    print(a)
    a=200
    print(a)
text1()
def text2():
    print(a)#调用全局变量a，默认使用全局变量
text2()









































