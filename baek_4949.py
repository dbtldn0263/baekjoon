while True:
    st=input()

    if st=='.':
        break

    arr=[]
    x=True

    for i in st:
        if i=='(' or i=='[':
            arr.append(i)

        elif i==')':
            if not arr or arr[-1]=='(':
                x=False
                break
        elif i==']':
            if not arr or arr[-1]=='[':
                x=False
                break

    if not arr and True:
        print('yes')

    else:
        print('no')