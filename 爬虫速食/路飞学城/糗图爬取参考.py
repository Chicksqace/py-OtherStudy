#
# # 需求：爬取糗事百科中糗图板块下所有的糗图图片
# import re
# import os
# import requests
# if __name__ == '__main__':
#      # 创建一个文件夹，保存所有的图片
#      if not os.path.exists('./qiutuLibs'):
#          os.mkdir('./qiutuLibs')
#      url = 'https://www.qiushibaike.com/imgrank/ '
#      headers = {
#          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#      }
#      # 使用通用爬虫对url对应的一整张页面进行爬取
#      page_text = requests.get(url=url, headers=headers).text
#      #print(page_text)
#      #使用聚焦爬虫将页面中所有的糗图进行解析提取
#      ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
#      img_src_list = re.findall(ex, page_text, re.S)
#      print(img_src_list)
#      for src in img_src_list:
#          #拼接出完整的图片url
#          src = 'https:' + src
#          img_data = requests.get(url = src, headers = headers).content
#          #生成图片名称
#          img_name = src.split('/')[-1]
#          imgPath = './qiutuLibs/' + img_name
#          with open(imgPath, 'wb') as fp:
#              fp.write(img_data)
#          print(img_name, '下载成功!')
# # 对上述代码进行进一步处理，使得能够分页爬取图片
#  if __name__ == '__main__':
#      # 创建一个文件夹，保存所有的图片
#      if not os.path.exists('./qiutuLibs'):
#          os.mkdir('./qiutuLibs')
#      # 设置一个通用的url模板
#      url = 'https://www.qiushibaike.com/imgrank/page/%d/'
#      for pageNum in range(1, 11):
#          # 对应页码的 url
#          new_url = format(url % pageNum)
#          headers = {
#          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#          }
#          # 使用通用爬虫对url对应的一整张页面进行爬取
#          page_text = requests.get(url=new_url, headers=headers).text
#          #print(page_text)
#          #使用聚焦爬虫将页面中所有的糗图进行解析提取
#          ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
#          img_src_list = re.findall(ex, page_text, re.S)
#          print(img_src_list)
#          for src in img_src_list:
#              #拼接出完整的图片url
#              src = 'https:' + src
#              img_data = requests.get(url = src, headers = headers).content
#              #生成图片名称
#              img_name = src.split('/')[-1]
#              imgPath = './qiutuLibs/' + img_name
#              with open(imgPath, 'wb') as fp:
#                  fp.write(img_data)
#              print(img_name, '下载成功!')