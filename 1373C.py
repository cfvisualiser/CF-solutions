for _ in range(int(input())):
    s=input()
    ans=len(s);cur=0
    for i in range(len(s)):
        if s[i]=="-":cur-=1
        else:cur+=1
        if cur<0:ans+=i+1;cur=0
    print(ans)
