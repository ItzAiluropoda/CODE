def NEWBILL():
    N=str(input("Enter customer Name:"))
    P=str(input("Enter customer Phone Number:"))
    m=str(input("Enter Payment method:"))
    global d
    d={"Name":N,"Phone Number":P,"Payment Method":m}
d={}
s={}
def MENU():
    global s
    while True:
        print('''To add new item press 1
        To remove Item press 2
        To stop press 3 ''')
        l=int(input("Enter your selection:"))
        if l==1:
            n=str(input("Enter Dish Name:"))
            p=int(input("Enter Dish Price:"))
            s.update({n.lower():p})
            print("Dish added")
        elif l==2:
            j=str(input("Enter name of Dish you wish to remove:"))
            if j.lower() in s:
                s.pop(j.lower())
                print("Dish removed")
            else:
                print("Dish not found")
        elif l==3:
            print(s)
            break