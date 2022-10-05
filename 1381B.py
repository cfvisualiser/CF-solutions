def solve():
    n=int(input())
    a=list(map(int,input().split()));flag=1
    c=0
    for i in range(n):
        if a[i]==1:
            c+=1
        else:
            break
    if c==n:
        if c%2:
            print("First")
        else:
            print("Second")
    else:
        flag=(c+1)%2
        if flag:
            print("First")
        else:
            print("Second")
for _ in range(int(input())):
    solve()
    
    
int q1=0;
for i in range(100):
    p=p+1;
    q1=q1*2;
return q1;

        

    

       
