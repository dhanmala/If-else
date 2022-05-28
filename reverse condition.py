a=int(input("enter the number"))
if a<1000 and a>99:
    b=a//10
    c=a%10
    d=b//10
    e=b%10
    c=str(c)
    e=str(e)
    d=str(d)
    print(c+e+d)
else:
    print("none")    
    