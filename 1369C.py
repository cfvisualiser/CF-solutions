for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort();f=n-1;c=0
    for i in range(k):
        if b[i]==1:
            c+=a[f]*2
            f-=1
        else:
            break
    f=0
    for j in range(k-1,i-1,-1):
        c+=a[f]+a[f+b[j]]
        f+=b[j]
    print(c)
        

