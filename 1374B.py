#solve function takes care of individual test cases
def solve():
    n=int(input())#take input
    flag=1#initialize
    c=0
    while n>1:
        if n%6==0:
            n//=6 #integer division
            c+=1  #increment
        elif n%3==0: 
            n*=2 #multiply n by 2
            c+=1 #increment
        else:
            flag=0 #keep flag as flase
            break
    if flag:
        print(c) #print c
    else:
        print(-1) #else print -1
for _ in range(int(input())):
    solve()
