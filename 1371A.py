def sticks_with_equal_length():
    for _ in range(int(input())):
        n=int(input())
        if n<=2:
            print(1)
        else:
            print((n+1)//2)

sticks_with_equal_length()
    