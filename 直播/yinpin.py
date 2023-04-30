import requests
import re
def get_music_url(music_id, music_title):
    url = 'https://api.zhuolin.wang/api.php'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=175aca5b31d39e-06d658eceb014a-3962420d-1fa400-175aca5b31e92e',
        'Host': 'api.zhuolin.wang',
        'Pragma': 'no-cache',
        'Referer': 'https://music.zhuolin.wang/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    params = {
        'callback': 'jQuery111305698848623906863_1604919341715',
        'types': 'url',
        'id': '{}'.format(music_id),
        'source': 'netease',
        '_': '1604919341751',
    }
    response = requests.get(url=url, params=params, headers=headers)
    html_data = response.text
    if music_url == '':
        print('无音频下载链接')

def music_id():
    url = 'https://music.163.com/discover/toplist'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    lis = re.findall('<li><a href="(.*?)">(.*?)</a></li>', response.text, re.S)[0:100]
    for i in lis:
        music_id = i[0].split('id=')[-1]
        title = i[1]
        pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]")  # '/ \ : * ? " < > |'
        music_title = re.sub(pattern, "_", title)  # 替换为下划线
        get_music_url(music_id, music_title)
    else:
        path = '保存地址\\' + music_title + '.mp3'
        response = requests.get(url=music_url)
        with open(path, mode='wb') as f:
            f.write(response.content)
            print(music_title, music_url)