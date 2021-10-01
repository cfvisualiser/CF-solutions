for _ in range(int(input())):
    n=int(input())
    s=input();f=-1;k=-1
    for i in range(n):
        if s[i]=="1":
            f=i
            break
    for j in range(n):
        if s[j]=="0":
            k=j
    if f>=k:
        print(s)
    else:
        print(s[:f]+s[k:])
