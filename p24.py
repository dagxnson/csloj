from math import *

n=int(input())
y_li=[]
tong_li=[]

for i in range(n):
    x, y=map(int, input().split())
    y_li.append(y)

max_y=max(y_li)
min_y=min(y_li)

for i in range(min_y, max_y):
    tong=0
    for j in range(n):
        tong=tong+fabs(i-y_li[j])
    tong_li.append(tong)

print(int(min(tong_li)))