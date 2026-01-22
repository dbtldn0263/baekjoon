n=int(input())

if n==0:
    print(0)
    exit()

level=[]
for i in range(n):
    level.append(int(input()))

level.sort()

d=round(n*0.15)

num=level[d:n-d]

result=round(sum(num)/len(num))

print(result)