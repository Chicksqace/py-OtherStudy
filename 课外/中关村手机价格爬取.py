import urllib.request
import re
'''
#######################################
网络爬虫：爬取中关村在线的手机型号及价格
Author: yangxiaolin
Date: 2018-12-29
#######################################
'''
def getHtml(url):
    # 获取网页内容
    page = urllib.request.urlopen(url)
    html = page.read()
    content = html.decode("GBK")
    return content

def getpage_num(content):
    #获取当前价格区间下总页数
    pattern_page = re.compile('<span class="small-page-active"><b>.*?</b>/(.*?)</span>',re.S)
    page_num = re.findall(pattern_page,content)
    page_num = int(page_num[0])
    return page_num

def getContext(content,price_gap_one):
    pattern = re.compile('<a href=.*?<img width.*?height=.*?alt="(.*?)".*?（.*?/a>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        if '（' in item:
            pattern_single = re.compile('(.*?)（.*?')
            item = re.findall(pattern_single,item)[0]
        print('正在写入：',str(item) + '\t' + str(price_gap_one) +'\n')
        f.write(str(item) + '\t' + str(price_gap_one) +'\n')

if __name__ == '__main__':
    f = open('device_price.txt', 'w+')
    price_class = [3000]
    price_gap = ['3000-3999']
    for price in price_class:
        content = getHtml('http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_%s_0_1_2_0_1.html'%(price))
        page_num = getpage_num(content)
        index = price_class.index(price)
        price_gap_one = price_gap[index]
        for page in range(1,page_num+1):
            content = getHtml('http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_%s_0_1_2_0_%s.html'%(price,page))
            getContext(content,price_gap_one)
    f.close()