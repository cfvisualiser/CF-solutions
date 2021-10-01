for _ in range(int(input())):
    n=int(input());e=0;o=0;b=[];c=[]
    a=list(map(int,input().split()))
    for i in range(2*n):
        if a[i]%2:o+=1;b+=[i+1]
        else:e+=1;c+=[i+1]
    if o%2 and e%2:
        e-=1;o-=1
    else:
        if e>o:e-=2
        else:o-=2
    for i in range(0,e,2):
        print(c[i],c[i+1])
    for i in range(0,o,2):
        print(b[i],b[i+1])
    
