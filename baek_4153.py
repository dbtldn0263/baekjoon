while 1:
    x,y,z=map(int,input().split())

    if x ==0 and y==0 and z ==0:
        break

    heru=sorted([x,y,z])

    if heru[0]**2+heru[1]**2==heru[2]**2:
        print('right')
    else:
        print('wrong')