N = int(input())

for i in range(N):
    n, s = input().split()
    for x in s:
        print(x*int(n), end='')
    print()  