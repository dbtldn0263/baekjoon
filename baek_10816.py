N=int(input())
arr1=list(map(int,input().split()))

M=int(input())
arr2=list(map(int,input().split()))

arr={}
for x in arr1:
   arr[x] = arr.get(x, 0) + 1

result = []
for x in arr2:
    result.append(arr.get(x, 0))

    
print(*result)