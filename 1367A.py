def solution():
    for _ in range(int(input())):
        t=input()
        b=t[0:2]
        if len(t)!=2:
            for i in range(3,len(t),2):
                b=b+t[i]
            print(b)
        else:
            print(t)
     
    
solution()
