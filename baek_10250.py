num=int(input())
for i in range(num):
    h,w,n=map(int,input().split())
    x=n//h+1
    f=n%h
    if f==0:
        x=n//h
        f=h
    print(f*100+x)