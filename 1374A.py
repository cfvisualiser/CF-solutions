for _ in range(int(input())):
    a,b,c=map(int,input().split())
    p=(c-b)//a
    q=p*a+b
    print(q)