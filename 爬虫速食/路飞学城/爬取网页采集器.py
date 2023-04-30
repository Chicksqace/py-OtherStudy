#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求载体身份标识为其某一游览器
#说明该请求是一个正常的请求，但是，如果检测到请求的载体身份标识不是某一游览器的，就表示该游览器不正常
#为不正常请求（爬虫），服务器端会拒绝该次请求
#UA:User-Agent(请求载体的身份标识)
#UA伪装：让爬虫对应的请求载体身份伪装成某一游览器
#一定要进行UA伪装
import requests
#UA伪装：将对应的User-Agen封装到一个字典中
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url='https://www.sogou.com/web'
#处理url所携带的参数：封装到字典中
kw=input('enter a word:')
param={
    'query':kw #https://www.sogou.com/web?query=%E6%B3%A2%E6%99%93%E5%BC%A0
}
#对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
response=requests.get(url=url,params=param,headers=headers)
page_text=response.text
filename=kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(filename,"保存成功")
