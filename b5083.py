S=input()
num_li=[]

for i in range(len(S)):
    if S[i].isnumeric()==False:
        S=S.replace(S[i], " ", 1)
S=" ".join(S.split())

print(S)