#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2022/1/1 21:55
# @Author : 不知天文，不知地理
# @File : 猜数.py
import random
num = random.randint(1,100)
number = input('猜一猜1-100之间系统选择的数吧！')
times = 1
while True:
  if times > 2:
    break
  if number.isnumeric():
    if int(number) == num:
      break
    if int(number) > num:
      number = input('不对哦，猜大了')
    else:
      number = input('不对哦，猜小了')
  else:
    number = input('需要在下方输入数字')
  times += 1

if times > 2 and int(number) != num:
  print('三次机会用完了')
else:
  print('恭喜你猜中了')
print('结果是' + str(num))