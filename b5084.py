n=int(input())
S=input()

max_ln=0
for i in range(n+1):
    for j in range(i, n+1):
        s=S[i:j]
        if s[::-1]==s:
            if len(s)>max_ln:
                max_ln=len(s)

print(max_ln)