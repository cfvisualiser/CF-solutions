from collections import Counter
for _ in range(int(input())):
    s=input();n=len(s)
    d=Counter(s);maxi=0
    for i in range(10):
        if d[str(i)]>maxi:
            maxi=d[str(i)]
    mini=min(n-maxi,n-2)
    for i in range(10):
        for j in range(i+1,10):
            ans1=0;ans2=0
            for k in range(0,n):
                if s[k]==str(i) and ans1%2==0:
                    ans1+=1
                elif s[k]==str(j) and ans1%2:
                    ans1+=1
                if s[k]==str(j) and ans2%2==0:
                    ans2+=1
                elif s[k]==str(i) and ans2%2:
                    ans2+=1
            if ans1%2:ans1-=1
            if ans2%2:ans2-=1
            mini=min(mini,n-ans1,n-ans2)
    print(mini)

                


    
