import requests
import json
url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
word=input('请输入查找的地区：')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
param={
    'cname': '',
    'pid': '',
    'keyword':word,
    'pageIndex':'1',
    'pageSize': '10'
}
response=requests.post(url=url,data=param,headers=headers)
list_data=response.text
with open('kfc.html','w',encoding='utf-8') as fp:
    fp.write(list_data)
print("over")