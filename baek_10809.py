s=input()
a='abcdefghijklmnopqrstuvwxyz'

for i in a:
    if i in s:
        print(s.index(i)) 
    else:
        print(-1)
        