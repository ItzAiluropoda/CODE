def expt6b():
    n=int(input("Enter a positive integer:"))
    factorial=1
    if n<0:
        print("Invalid input")
    else:
        while True:
            if n==0:
                break
            factorial=factorial*n
            n=n-1
        print(factorial,"is the factorial")
def expt7a():
    n=int(input("Enter a numebr 1:"))
    k=int(input("Enter a number 2:"))
    p=int(input("Enter a number 3:"))
    digit=[n,p,k]
    for i in digit:
        for j in digit:
            for o in digit:
                if (i!=j and i!=o and o!=j):
                    print(i,j,o)
def expt9a():
    string=input("Enter a string:")
    count=0
    for i in string:
        if i.upper() in ["A","E","I","O","U"]:
            count=count+1
    print(count)