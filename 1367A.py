def solve():
    for _ in range(int(input())):
        t=input()
        b=t[0:2]
        if len(t)==2:
            print(t)
        else:
            for i in range(3,len(t),2):
                b+=t[i]
            print(b)
     
    
solve()
