def solve:
    for _ in range(int(input())):
        m=int(input())
        a=list(map(int,input().split()));e=0;o=0
        for i in range(m):
            if i%2:
                if a[i]%2!=1:
                    e+=1
            else:
                if a[i]%2!=0:
                    o+=1
        if e==o:
            print(e)
        else:
            print(-1)
      s+=1
      p+=1
solve()
