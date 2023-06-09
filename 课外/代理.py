# import requests
# from bs4 import BeautifulSoup
#
# # 构造请求头
# headers = {
#     'User-Agent': '伪装头'}
#
# # 构造URL
# url = 'http://www.66ip.cn/'
#
# # 发送GET请求
# response = requests.get(url, headers=headers)
#
# # 解析HTML
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # 获取所有代理地址
# proxy_list = []
# table = soup.find('table', attrs={'bordercolor': '#6699ff'})
# if table is not None:
#     tr_list = table.find_all('tr')[1:]
#     for tr in tr_list:
#         td_list = tr.find_all('td')
#         if len(td_list) >= 2:
#             ip = td_list[0].text.strip()
#             port = td_list[1].text.strip()
#             proxy_list.append(f'{ip}:{port}')
#
# # 输出代理地址列表
# print(proxy_list)

import requests
from bs4 import BeautifulSoup

# 伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# 多页面爬取
url_template = 'http://www.66ip.cn/{}.html'
# 遍历前n页
n=6
proxy_list = []
for page in range(1, n):
    url = url_template.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', attrs={'bordercolor': '#6699ff'})
    if table is not None:
        tr_list = table.find_all('tr')[1:]
        for tr in tr_list:
            td_list = tr.find_all('td')
            if len(td_list) >= 2:
                ip = td_list[0].text.strip()
                port = td_list[1].text.strip()
                proxy_list.append(f'{ip}:{port}')

print(proxy_list)