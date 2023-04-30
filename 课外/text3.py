import requests
from bs4 import BeautifulSoup

resp=requests.get('https://www.baidu.com')
print(resp)
print(resp.content)
bsobj=BeautifulSoup(resp.content,'lxml')
a_list=bsobj.find_all('a')
text=''
for a in a_list:
    href=a.get('href')
    text+=href+'\n'
with open('baidu.com','w') as f:
    f.write(text)
