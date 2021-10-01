for _ in range(int(input())):
    n=int(input())
    if n>30:
        if n-30!=6 and n-30!=10 and n-30!=14:
            print("YES")
            print(6,10,14,n-30)
        elif n-30==6 and n-30!=10 and n-30!=14:
            print("YES")
            print(6,10,15,5)
        elif n-30!=6 and n-30!=10 and n-30==14:
            print("YES")
            print(6,7,10,21)
        elif n-30!=6 and n-30==10 and n-31!=14:
            print("YES")
            print(6,14,15,5)
        else:
            print("NO")
    else:
        print("NO")

