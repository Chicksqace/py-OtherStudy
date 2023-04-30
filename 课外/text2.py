import requests
from bs4 import BeautifulSoup

# #获取图片   输入网址
req=requests.get("https://blog.csdn.net/a1439775520/article/details/95373610")
#获取网址的html
html=req.text
#print(html)
#使用beautifulsoup接受这个html
soup=BeautifulSoup(html,"html.parser")
#加入count是为了有多张图片，防止名字相同被替换掉
count=0
#for循环   找到所有img标签   获取其他元素也可以写别的标签
for img in soup.find_all("img"):
#得到他的src属性
    src=img.get("src")
    print(src)
    #请求src的路径
    req=requests.get(src)
    #在这里传入你想保存的文件夹
    with open('D:\\PyCharm_Filr\\temp/' + str(count) + '.jpg', 'wb') as f:
        #req.content就是获取src的内容，就是他的图片
        f.write(req.content)
    count=count+1