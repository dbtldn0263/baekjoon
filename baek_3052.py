result=[]

for i in range(1,11):
    num=int(input())
    result.append(num%42)
x=set(result)
print(len(x))