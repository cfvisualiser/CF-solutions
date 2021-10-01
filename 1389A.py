import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x*2<=y:
        print(x,2*x)
    else:
        print(-1,-1)