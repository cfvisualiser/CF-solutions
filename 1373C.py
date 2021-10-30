def get_res_value():
    for _ in range(int(input())):
        s=input()
        ans=len(s)
        cur=0
        n=len(s)
        #forloop
        for i in range(0,n):
            if s[i]=="-":
                cur=cur-1 #update cur
            else:
                cur=cur+1 #update cur
            if cur<0:
                ans=ans+i+1 #update ans
                cur=0
        print(ans)


get_res_value()
