num=map(int,input().split())

result=0

for i in num:
    k=i**2

    result=result+k

print(result%10)