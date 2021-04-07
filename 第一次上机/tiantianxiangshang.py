'''
Author: martin
Date: 2020-09-17 15:49:07
LastEditTime: 2020-09-17 16:12:08
LastEditors: Please set LastEditors
Description: tiantianxiangshang
FilePath: /py/work/tiantianxiangshang.py
'''
import math

yeardays=365
rate=0.01
level=1

n=input("一周工作多少天：")

for day in range(yeardays):
    if (day+1)%7==0 or (day+1)%6==0:
        level-=level*rate
    else:
        level+=level*rate

print("一年每周休息2天，工作五天，能力值提升：%s"%(level))






