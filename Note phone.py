def menu():
    print("1.Add")
    print("2.Search")
    print("3.Edit")
    print("4.Delete")
    print("5.All")
    print("6.Exit")
Name=[]
Famely=[]
Home=[]
Mobile=[]
Address=[]
Mobile2=[]
def add(Name,Famely,Home,Mobile,Address,Mobile2):
    x= input("Plz enter name :")
    Name.append(x)
    x= input("Plz enter famely :")
    Famely.append(x)
    x= input("Plz enter Home number :")
    Home.append(x)
    x= input("Phone number = ")
    Mobile.append(x)
    x= input("Add address = ")
    Address.append(x)
    x= input("Phone number2 :")
    Mobile2.append(x)
def Search():
       search=input("Plz enter name = ")
       famely=input("plz enter famely = ")
       if search in Name and famely in Famely:
            num=Famely.index(famely)
            print("----------------------------")
            print("name =",Name[num])
            print("famely =",Famely[num])
            print("home number =",Home[num])
            print("mobile number =",Mobile[num])
            print("address =",Address[num])
            print("mobile number2 =",Mobile2[num])
            print("-------------------------------")
       else:
            print("Not found")
def Edit():
    name=input("Plz enter name : ")
    famely=input("plz enter famely : ")
    if name in Name and famely in Famely:
        num=Famely.index(famely)
        print("----------------------------")
        print("name =",Name[num])
        print("famely =",Famely[num])
        print("home number =",Home[num])
        print("mobile number =",Mobile[num])
        print("address =",Address[num])
        print("mobile number2 =",Mobile2[num])
        print("-------------------------------")
        print("")
        print("")
        print("")
        print("1.cheng name")
        print("2.cheng famely")
        print("3.cheng home number")
        print("4.cheng mobile number")
        print("5.cheng address")
        print("6.cheng mobile number2")
        edit=int(input("input one number = "))
        if edit==1:
            name=input("plz enter new name = ")
            Name[num]=name
        elif edit==2:
            famely=input("plz enter new famely = ")
            Famely[num]=famely
        elif edit==3:
            home=input("plz enter new home number = ")
            Home[num]=home
        elif edit==4:
            mobile=input("plz enter new mobile number = ")
            Mobile[num]=mobile
        elif edit==5:
            address=input("plz enter new adddress = ")
            Address[num]=address
        elif edit==6:
            mobile2=input("plz enter new mobile number2 = ")
            Mobile2[num]=mobile2       
def Delete():
    name=input("plz enter name : ")
    famely=input("plz enter famely : ")
    if name in Name and famely in Famely:
        num=Famely.index(famely)
        del Name[num]
        del Famely[num]
        del Home[num]
        del Mobile[num]
        del Address[num]
        del Mobile2[num]
    else:
        print("Not Fuond!")
def show_all(Name,Famely,Home,Mobile,Address,Tell2):
    for i in range(len(Name)):
        print("-------------------------")
        print("name =",Name[i])
        print("famely =",Famely[i])
        print("home number =",Home[i])
        print("mobile number =",Mobile[i])
        print("address =",Address[i])
        print("mobile number2 =",Mobile2[i])
        print("-------------------------")

while True:
    menu()
    Menu=int(input("input one number = "))
    if Menu==1:
        add(Name,Famely,Home,Mobile,Address,Mobile2)     
    if Menu==2:
        Search()
    if Menu==3:
        Edit()
    if Menu==4:
        Delete()   
    if Menu==5:
        show_all(Name,Famely,Home,Mobile,Address,Mobile2)
    if Menu==6:
        break
