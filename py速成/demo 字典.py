# #字典的定义
# info={"name":"城市","age":14}
# #字典的访问
# print(info["name"])
# #访问了不存在的键
# #print(info["gender"]) #直接访问会报错
# #print(info.get("gender"))#使用get()方法默认返回：None
# print(info.get("gender",1))#没找到时可以设置默认值
# print(info.get("name"))
#增
'''
newID=input("请输入学号")
info={"name":"城市","age":14}
info["id"]=newID
print(info["id"])
'''



#删
#[del]
# info={"name":"城市","age":14}
# print("删除前:%s"%info["name"])#删除了指定键值之后，再次访问会报错
# del info['name']
# print("删除后：s%"%info['name'])
# info={"name":"城市","age":14}
# print("删除前:%s"%info["name"])
# del info#删除字典后报错
# print(info)
#【clear】
'''
info={"name":"城市","age":14}
print("清空前:%s"%info)
info.clear()#整个字典
print("清空后:%s"%info)
'''
#改
'''
info={"name":"城市","age":14}
info['age']=15
print(info)
'''



#改
info={"id":1,"name":"城市","age":14}
# print(info.keys())#所以的键{列表}
# print(info.values())#所以的值{列表}
# print(info.items())#得到所有的值（列表）,每个键值都是一个元组


#遍历所有的值
# for key in info.keys():
#     print(key)
# for values in info.values():
#     print(values)
# for key,value in info.items():
#     print("key=%s,value=%s"%(key,value))
#使用枚举函数，同时拿到列表的下标和元素内容
mylist=['a','b','c','d']
for i,x in enumerate(mylist):
    print(i+1,x)
#集合就是key,没有值
