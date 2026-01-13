L=int(input())
str=input()

r = 31
M = 1234567891

result = 0

for i in range(L):
    value = ord(str[i]) - ord('a') + 1
    result += value * (r ** i)

print(result % M)