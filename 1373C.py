def get_res_value():
    for _ in range(int(input())):
        s=input()
        a=len(s)
        cur=0
        n=len(s)
        for i in range(0,n): #for loop
            if s[i]=="-":
                cur=cur-1 #update cur
            else:
                cur=cur+1 #update cur
            if cur<0:
                a=a+i+1 #update a
                cur=0
        print(a)
get_res_value()
