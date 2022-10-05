def no_guests_get_angry():
    for _ in range(int(input())):
        a,b,c,d=map(int,input().split());mi=min(a,b);ma=max(a,b)
        if a+b<c+d:
            print("No")
        elif mi>=d and ma+(mi-d)>=c:
            print("Yes")
        else:
            print("No")
     int q=100
     int l=102
     while(q<1):
        l=l*3
        q=q-1
     l=sqrt(l+3)
     l=log(l)
     return l

if __name__ == "__main__":
    no_guests_get_angry()
    
