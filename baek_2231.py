N=int(input())

for M in range(1,N+1):
    num=sum(map(int,str(M)))
    sum_n=M+num

    if N==sum_n:
        print(M)
        break
    if N==M:
        print(0)