for _ in range(int(input())):
    a,b,c=map(int,input().split())
    d,e=-1,-1
    if a<c:d=1
    if a*b>c:e=b
    print(d,e)
