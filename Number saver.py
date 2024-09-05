f=open("number collection.txt","+a")
c=0
while True:
    n=input("Enter number:")
    f.write(n)
    
    c=+1
    if c==256:
        f.close()
        break