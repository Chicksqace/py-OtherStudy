# # 3．使用re模块，对如下所给文本段落，请采用多行模式，只匹配全文开头的英文单词，
# # 再匹配全文每一行开头的英文单词。要求用findall方法来做。
# import re
# s="I love China,notonlybecause\n12sd34er56\ndfe456636\nsheisold,butalsobecausesheisgreat"
# a=re.findall(r'^[a-zA-Z]+',s,re.M)
# b=re.findall(r'^[a-zA-Z]+',s,re.S)
# print('多行首单词',a)
# print('单行首单词',b)
# # 7．（习题8）使用re模块findall函数，编写一个正则表达式，对如下所给网页文件，
# # 提取（1）所有图片链接；（2）所有图片大小；（3）所有图片的宽度与高度，并全部
# # 打印输出。
# """<cc><divid="post_content_115101375872"class="d_post_content
# j_d_post_content">秋高气爽<br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=16a7318cd2f9d72a
# 17641015e42b282a/353680cb39dbb6fd5e8db0950224ab18952b379e.jpg"
# size="65387"changedsize="true"width="560"height="420"
# size="65387"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=80df3901b9b7d0a2
# 7bc90495fbee760d/1ddd0b55b319ebc49aae232a8926cffc1c17169e.jpg"
# size="50323"changedsize="true"width="560"height="420"
# size="50323"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=078b542b55df8db1
# bc2e7c6c3922dddb/33c010dfa9ec8a1338cc0253fc03918fa2ecc09f.jpg"
# size="78770"changedsize="true"width="560"height="373"
# size="78770"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=f4602793b212c8fcb
# 4f3f6c5cc0292b4/b0c62934349b033bdd5ea9691ece36d3d739bd9f.jpg"
# size="95035"changedsize="true"width="560"height="373"
# size="95035"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=1f8f63cc73f0f736d8
# fe4c093a54b382/300b37d12f2eb9382fbb2f41de628535e7dd6f9f.jpg"
# size="100285"changedsize="true"width="560"height="373"
# size="100285"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=cf96d68331f33a879
# e6d0012f65d1018/6b5f0e2442a7d933d23ab1c0a64bd11371f001da.jpg"
# size="65247"changedsize="true"width="560"height="420"
# size="65247"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=dfff2f41de62853592
# e0d229a0ee76f2/4a9f8ad4b31c8701e524e7552c7f9e2f0508ffdb.jpg"
# size="79750"changedsize="true"width="560"height="414"
# size="79750"><br><imgclass="BDE_Image"
# src="https://imgsa.baidu.com/forum/w%3D580/sign=b4a6d35d9782d158
# bb8259b9b00b19d5/35d1279759ee3d6d3054d27848166d224d4adedb.jpg
# "size="103175"changedsize="true"width="560"height="414" size="103175"></div><br></cc><a href="https://www.baidu.com"></a>
# """
list1=[4,5,6]
list2=list1
list1[2]=3
print(list2)