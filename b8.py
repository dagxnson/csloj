ar_len=int(input())
ar=input().split(" ")

def lTron(x, y):
    n_li=str(float(x)).split(".")
    if n_li[1]=="0":
        dec_num=str(10**y)[1:]
        return n_li[0]+"."+dec_num
    elif len(n_li[1])>y:
        dec_num=n_li[1][:y]
        return n_li[0]+"."+dec_num
    elif len(n_li[1])<y:
        dec_num=str(int(n_li[1])*(10**(y-len(n_li[1]))))
        return n_li[0]+"."+dec_num
    return x

li=[]
tb_li=[]

for x in range(ar_len):
    li.append(int(ar[x]))

for i in range(ar_len-1):
    for j in range(i+1, ar_len):
        T=0
        for k in range(i, j+1):
            T=T+li[k]
        tb=T/(j-i+1)
        tb_li.append(tb)

max_val=max(tb_li)
min_val=min(tb_li)

print(lTron(min_val, 3)+" "+lTron(max_val, 3))