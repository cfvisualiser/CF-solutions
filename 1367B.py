for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()));e=0;o=0
    for i in range(n):
        if i%2:
            if a[i]%2!=1:
                e+=1
        else:
            if a[i]%2!=0:
                o+=1
    if e==o:
        print(e)
    else:
        print(-1)

