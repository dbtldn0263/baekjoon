isbn = list(input().strip())

idx = isbn.index('*')

total = 0
for i in range(13):
    if isbn[i] == '*':
        continue
    num = int(isbn[i])
    if i % 2 == 0:
        total=total+num
    else:
        total=total+(num * 3)

if idx%2==0:
    w=1
else:
    w=3

for x in range(10):
    if (total + x * w) % 10 == 0:
        print(x)
        break