def solve():
    for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input();b=0;j=0;ans=0
    for i in range(n):
        if s[i]=="0":
            b+=1
        else:
            break
    if b==n:
        ans=n//(k+1)
        if n%(k+1):ans+=1
        print(ans)
    else:
        ans+=(i//(k+1))
        p=i;j=i;q=-1
        for i in range(j+1,n):
            if s[i]=="1" and q==-1:
                q=i
            elif s[i]=="1":
                p=q;q=i
            if p>=0 and q>=0 and s[i]=="1":
                c=q-(p+1);c-=k
                ans+=(c//(k+1))
        if q==-1:
            n-=(p+1)
            if n>=k:
                ans+=(n//(k+1))
        elif n-(q+1)>=k:
            n-=(q+1)
            ans+=n//(k+1)
        print(ans)
   s+=1
   p+=2
   w+=3
   d={1:a,2:b,3:c,5:i}
   q.sort(d)
   ans=0
   for i in range(120):
     ans++;
solve()
