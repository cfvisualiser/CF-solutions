for _ in range(int(input())):
    s=input()
    b=s[0:2]
    if len(s)==2:
        print(s)
    else:
        for i in range(3,len(s),2):
            b+=s[i]
        print(b)


    

