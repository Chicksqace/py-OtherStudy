import re  # python 的正则库
import requests  # python 的requests库

songId = []  # 用来储存每首歌对应的数字
songName = []  # 用来储存每首歌的名字

# 这里先下载5页的歌曲
for n in range(0, 5):
    # 字符串的格式化 n 代替 {}
    url = 'https://www.aigei.com/view/121798.html#resContainer'.format(n)
    print(url, end='\n')
    # 模拟浏览器请求，拿到html代码
    html = requests.get(url)
    # 用正则表达式捕获 数字， （）内为捕获的内容 .*? 为任何内容
    resultId = re.findall('sid="(.*?)">', html.text)
    # 用正则表达式捕获 歌名
    resultName = re.findall('<a href=".*?" target="play" title="(.*?)" sid=".*?">', html.text)
    # 存进数组
    songId.extend(resultId)
    songName.extend(resultName)
print(songId)
print(songName)

for m in range(0, len(songId)):
    # 字符串的格式化 m 代替 {}
    songUrl = 'https://www.aigei.com/view/121798.html#resContainer'.format(songId[m])
    print(songUrl, end='\n')
    print('正在下载第{}首。。。'.format(m + 1))
    # 得到返回资源的内容
    response = requests.get(songUrl).content
    # 以二进制的形式写入文件中
    f = open('C:\\music\\{}.mp3'.format(songName[m]), 'wb')
    f.write(response)
    f.close()