while True:
    try:
        print("Enter 1 to order \nEnter 2 change menu \nEnter 3 to print Bill \nEnter 4 to Quit")
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
    except:
        print("Wrong input try again")
d,o={},{}
s={"cake":70, "juice":30, "milkshake":60, "rice":80, "dal":110, "snack":20}
def NEWBILL():
    global d,o
    o,d,t={},{},0
    N=str(input("Enter customer Name:"))
    P=str(input("Enter customer Phone Number:"))
    m=str(input("Enter Payment method:"))
    print("Menu")
    for x in s:
        print(x,":",s[x])
    while True:
        print("Enter name name of Dish to order, Enter 1 to end order")
        k=(input("Enter Dish:")).lower()
        if k in s:
            q=int(input("Enter Quantity:"))
            o[k]=[s[k],q]
            t=t+s[k]*q
            print("Your Order")
            for v in o:
                print(j,o[j][1])
            print("Your Total:",t)
        elif k=="1":
            print("Your Order")
            for j in o:
                print(j,o[j][1])
            print("Your Total:",t)
            print("Thank you",N)
            break
        else:
            print("Dish not Found")
    d={"Name":N,"Phone Number":P,"Payment Method":m,"Total":t}
def MENU():
    global s
    while True:
        try:
            print("To add new item press 1 \nTo remove Item press 2 \nTo stop press 3 ")
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
        except:
            print("Wrong input try again")