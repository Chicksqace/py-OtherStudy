#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2021/12/11 12:23
# @Author : 陈攀宇
# @File : 国家药品监督管理局2.py
import requests
import json
#获取不同企业的ID值
url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
#参数的封装
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
id_list=[]#存储企业的ID
all_data_list=[]#存储所以企业的详情数据
for page in range(1,5):
    page=str(page)
    data={
        "on": "true",
        "page": page,
        "pageSize": 15,
        "productName":"" ,
        "conditionType": "1",
        "applyname":"" ,
        "applysn": "",
    }
    json_ids=requests.post(url=url,headers=headers,data=data).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
#获取企业详情数据
post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data={
    "id": id
}
    datail_json=requests.post(url=post_url,headers=headers,data=data).json()
    all_data_list.append(datail_json)
    #进行持久化存储
fp=open("./国家药品监督管理局2.json","w",encoding="utf-8")
json.dump(all_data_list,fp=fp,ensure_ascii=False)
print("over!!")