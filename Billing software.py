def NEWBILL():
    global d
    global o
    o={}
    d={}
    t=0
    N=str(input("Enter customer Name:"))
    P=str(input("Enter customer Phone Number:"))
    m=str(input("Enter Payment method:"))
    while True:
        print("Enter name name of Dish to order, Enter 1 to end order")
        k=str(input("Enter Dish:"))
        if k.lower() in s:
            q=int(input("Enter Quantity:"))
            o[k]=[s[k],q]
            t=+s[k]*q
        elif k==1:
            break
        else:
            print("Dish not Found")
    d={"Name":N,"Phone Number":P,"Payment Method":m,"Total":t}
d={}
s={"cake":70, "Juice":30, "Milkshake":60, "Rice":80, "Dal":110, "Snack":20}
o={}
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
while True:
    print("Enter 1 to order \n Enter 2 change menu \n Enter 3 to print Bill \nEnter 4 to Quit")
    j=int(input("Enter:"))
    if j==1:
        NEWBILL()
    elif j==2:
        MENU()
    elif j==3:
        print("Print system not setup")
    elif j==4:
        break
    else:
        print("Wrong input try again")