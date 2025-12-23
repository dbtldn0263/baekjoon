h,m=map(int,input().split())
rm=m-45

if rm<0:
    h=h-1
    rm=60+rm
if h<0:
    h=h+24
print(h,rm)