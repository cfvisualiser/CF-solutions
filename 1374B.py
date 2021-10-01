for _ in range(int(input())):
    n=int(input())
    flag=1;c=0
    while n>1:
        if n%6==0:
            n//=6
            c+=1
        elif n%3==0:
            n*=2
            c+=1
        else:
            flag=0;break
    if flag:
        print(c)
    else:
        print(-1)