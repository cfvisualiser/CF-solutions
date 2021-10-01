for _ in range(int(input())):
    s=input()
    zero,one=0,0
    for i in range(len(s)):
        if s[i]=="0":zero+=1
        else:one+=1
    ans=min(zero,one)
    if ans%2:print("DA")
    else:print("NET")