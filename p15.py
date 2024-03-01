from math import *
n=int(input())
a=input().split()
a=list(set(a))
u_li=[]
def timUoc(n):
    u_li=[]
    x=int(sqrt(n)+1)
    for i in range(1, x):
        if x%i==0:
            u_li.append(i)
            u_li.append(int(x/i))
    return u_li
for i in range(len(a)):
    u_li=u_li+timUoc(int(a[i]))
res=len(list(set(u_li)))
print(res)