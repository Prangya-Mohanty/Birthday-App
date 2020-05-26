dict={}
while True:
    print("--------------------------Birthday App---------------------------------")
    print("1.Add  to Birthday List")
    print("2.Show Birthday")
    print("3.Exit")
    choice=int(input("Enter the Choice"))
    if choice == 2:
        if len(dict.keys())==0:
            print("Nothing To Show")
        else:
            name=input("Enter Name to Look For Birthday")
            birthday=dict.get(name,"No Data Found")
            print(birthday)
    elif choice == 1:
          name=input("Enter Friend Name")
          date=input("Enter Birthday Date")
          dict [name]=date
          print("Birthday Added")
    elif choice == 3:
        break
    else:
        print("Choose a Valid Option")

