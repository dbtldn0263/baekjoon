import sys

N=int(sys.stdin.readline())
num=[0]*100001

for i in range(N):
    num[int(sys.stdin.readline())]+=1

for j in range(100001):
    if num[j] !=0:
        for k in range(num[j]):
            print(j)

# import sys
 
# N = int(sys.stdin.readline())
# num_list = [0] * 100001
 
# for _ in range(N):
#     num_list[int(sys.stdin.readline())] += 1
 
# for i in range(100001):
#     if num_list[i] != 0:
#         for _ in range(num_list[i]):
#             print(i)