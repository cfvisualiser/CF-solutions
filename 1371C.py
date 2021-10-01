for _ in range(int(input())):
    a,b,c,d=map(int,input().split());mi=min(a,b);ma=max(a,b)
    if a+b<c+d:
        print("No")
    elif mi>=d and ma+(mi-d)>=c:
        print("Yes")
    else:
        print("No")
    
