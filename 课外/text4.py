"""请求网页"""
import re

import  requests
response=requests.get('http://desk.tooopen.com/meinv_3_2.html')
#print(response.text)
htm1=response.text
"""解析网页"""
urls=re.findall('< a href="(.*?)" target=".*?">',htm1)
print(urls)
"""保存图片"""
for url in urls:
    #time.sleep(1)
    #图片的名字
    file_name=url.split('/')[-1]
    response=requests.get(url)
    with open(file_name,'wb') as f:
        f.write(response.content)