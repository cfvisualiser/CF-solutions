def solve:
    for _ in range(int(input())):
        m=int(input())
        if m>30:
            if m-30!=6 and m-30!=10 and m-30!=14:
                print("YES")
                print(6,10,14,m-30)
            elif m-30==6 and m-30!=10 and m-30!=14:
                print("YES")
                print(6,10,15,5)
            elif m-30!=6 and m-30!=10 and m-30==14:
                print("YES")
                print(6,7,10,21)
            elif m-30!=6 and m-30==10 and m-31!=14:
                print("YES")
                print(6,14,15,5)
            else:
                print("NO")
        else:
            print("NO")

solve();
