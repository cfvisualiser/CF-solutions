for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=["a"*50];val=98
    for i in range(n):
        s=(b[i][0:a[i]])
        if chr(val)==b[i][-1]:
            val+=1
            if val==123:
                val=97
        s+=chr(val)*(50-a[i])
        b+=[s]
        val+=1
        if val==123:
            val=97
    for i in range(n+1):
        print(b[i])