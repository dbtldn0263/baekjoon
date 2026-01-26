N=int(input())
num=[]
for _ in range(N):
    x=int(input())
    num.append(x)

avg=sum(num)/N

num.sort()
mid=num[N//2]

dic = {}
for x in num:
    dic[x] = dic.get(x, 0) + 1

mx= max(dic.values())

arr = []
for k, v in dic.items():
    if v == mx:
        arr.append(k)

arr.sort()
mm = arr[0] if len(arr) == 1 else arr[1]


ran=max(num)-min(num)



print(round(avg))
print(mid)
print(mm)
print(ran)