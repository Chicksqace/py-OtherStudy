#post请求（携带的参数）
#响应数据是一组json数据
import requests
import json
#1.指定url
post_url='https://fanyi.baidu.com/sug'
#2.UA伪装：将对应的User-Agen封装到一个字典中
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#3.post请求参数处理（同get请求一致）
word=input('enter a word :')
data={
    'kw':word
}
#4.请求发送
response=requests.post(url=post_url,data=data,headers=headers)
#5.获取响应数据:json()方法返回是obj(对象)（如果确认响应数据是json类型的，才能使用json（））
dic_obj=response.json()
#print(dic_obj)#获取字典对象
#进行持久化存储
filename=word+'.json'
fp=open(filename,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
print('over!!!')
