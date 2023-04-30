import requests
import json
url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
#index=input('输入查找的页数：')
word=input('请输入查找的地区：')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Origin': 'http://www.kfc.com.cn',
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
}
param={
    'cname':word,
    'pid': '',
    'pageIndex':'1',
    'pageSize': '10'
}

response=requests.post(url=url,data=param,headers=headers)
data = json.loads(response.text)
#with open('kfc.json','w',encoding='utf-8')as f:
#    f.write(str(json.loads(response.text)))
storeName=[];addressDetai=[];pro=[]
#print(data)
print('>'*20)
for num in range(0,9):
    storeName.append(data['Table1'][num]['storeName'])
    addressDetai.append(data['Table1'][num]['addressDetail'])
    pro.append(data['Table1'][num]['pro'])
print(storeName)
print('>'*20)
print(addressDetai)
print('>'*20)
print(pro)
print('>'*20)
print("over")
