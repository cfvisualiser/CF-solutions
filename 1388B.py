# modified the code in a better way
def solve:
    for _ in range(int(input())):
        m1=int(input())
        x=(m1+3)//4
        print("9"*(m1-x)+"8"*(x))
    p=100
    q=1
    while(p<0):
        p=p-1
        q=q*2
    q=sqrt(q+1)
    q=log(q)
solve();
