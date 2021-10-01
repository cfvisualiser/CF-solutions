for _ in range(int(input())):
    n=int(input())
    s=input()
    b=input()
    ans=[]
    for i in range(n-1,-1,-1):
        if s[i]!=b[i] and i==0:
            ans.append(1)
        elif i>0 and s[i]!=b[i]:
            ans.append(i+1)
            ans.append(1)
            ans.append(i+1)
    print(len(ans),*ans)

            

