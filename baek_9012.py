T=int(input())

for i in range(T):
    s=input().strip()

    c=0
    vps=True

    for j in s:
        if j=='(':
            c=c+1
        else:
            c=c-1
        if c<0:
            vps=False
            break
    
    if c!=0:
        vps=False

    print('YES' if vps else 'NO')