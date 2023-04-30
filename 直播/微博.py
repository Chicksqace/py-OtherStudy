import os
import pprint
import requests


def get_response(html_url):
    headers = {
        'Cookie': 'audio_play_last_item=31695486; audio_play_last_position=7199.785000000001; gei_d_u=a06077f780a141f5a6c92215873e6d81; oOO0OO0oOO00oo0o=true; SESSION=45c40f1d-f9f1-4fec-b48c-e67ecc542976; OooOO000oOOO00o=be9462882d2d4d649b3dfab89b4126da; geiweb-v=zZ+S93HA1QekGnx5DT9aIJ/Y55LP745bl3pm0y22DwiHqhpOlnw9zqt0B98HHvXw; SERVERID=7a053a6764ffb4a646529948ff8759c9|1655435768|1655434944',
        'csrf': 'D2YF7NMH81N',
        'Referer': 'https://www.aigei.com/view/121798.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def get_music_info(html_url):
    json_data = get_response(html_url).json()
    pprint.pprint(json_data)
    music_list = json_data['data']['musicList']
    for index in music_list:
        music_name = index['album']
        singer = index['artist']
        music_rid = index['rid']


if __name__ == '__main__':
    url = 'https://www.aigei.com/view/121798.html'
    get_music_info(url)
def get_music_url(music_rid):
    page_url = f'https://www.aigei.com/view/121798.html?page={music_rid}#resContainer'
    json_data = get_response(page_url).json()
    music_url = json_data['url']
    return music_url
def save(music_name, music_url):
    path = 'music\\'
    if not os.path.exists(path):
        os.makedirs(path)
    filename = path + music_name + '.mp3'
    headers = {
        'if-range': '8eba7fc5d5b2f4d223d54612aa3f4773',
        'range': 'bytes=524288-524288',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
    }
    music_content = requests.get(url=music_url, headers=headers).content
    with open(filename, mode='wb') as f:
        f.write(music_content)
        print('正在保存：', music_name)
