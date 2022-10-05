import math
def solve:
    for _ in range(int(input())):
        x,y=map(int,input().split())
        if not x*2<=y:
            print(-1,-1)
            continue
        print(x,2*x)

solve();
