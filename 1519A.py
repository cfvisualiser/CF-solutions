for t in range(int(input())):
    d = list(map(int,input().split(' ')))
    if d[0]<d[1]:
        if (d[2]+1)*d[0]>=d[1]:
            print('YES')
            continue
        else:
            print('NO')
    else:
        if (d[2]+1)*d[1]>=d[0]:
            print('YES')
            continue
        else:
            print('NO')
