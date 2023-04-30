'''
print("____________1")
f= open("123.tet", "r")#用只读模式打开一个不存在的文件，报错
print("____________2")#这句代码不会执行
'''
#捕获异常

'''
try:
    print("____________1")
    f=open("123.tet","r")
    print("____________2")
except IOError:  #文件没找到，属于IO异常（输入输出异常）
    pass        #捕获异常后，执行的代码
'''
'''
try:
    print(num)
#except IOError: #异常错误想要被捕获，需要一致
except NameError:
    print("产生错误了")
'''
'''
try:
    print("____________1")
    f=open("123.tet","r")
    print("____________2")
    print(num)
#except IOError: #异常错误想要被捕获，需要一致
except (NameError,IOError):#将可能产生的所有的异常类型，都放到下面的小括号中
    print("产生错误了")
'''
'''
#获取错误描述
try:
    print("____________1")
    f=open("123.tet","r")
    print("____________2")
    print(num)
#except IOError: #异常错误想要被捕获，需要一致
except (NameError,IOError) as result:#将可能产生的所有的异常类型，都放到下面的小括号中
    print("产生错误了")
    print(result)
'''
'''
#捕获所有异常
try:
    print("____________1")
    f=open("123.tet","r")
    print("____________2")
    print(num)
#except IOError: #异常错误想要被捕获，需要一致
except Exception as result:#Exception 可以承接任何异常
    print("产生错误了")
    print(result)
'''


#tey.......finally 和嵌套
import time
try:
    f=open("test1.txt","r")

    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:#一定会被执行
        f.close()
        print("文件关闭")



except Exception as result:
    print("发生异常")
























