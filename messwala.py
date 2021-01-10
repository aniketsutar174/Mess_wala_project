mess1_menu=[]
mess2_menu=[]

mess1_cnt=0
mess2_cnt=0
mess_name1=input("Enter 1st name of mess..:-")
mess_name2=input("Enter 2nd name of mess..:-")

while True:

    if mess1_cnt == 3 and mess2_cnt == 3:
        #print(mess1_menu)
        #print(mess2_menu)
        break
    else:
        name = input("What is ur mess name?\n")
        if name == mess_name1:
            for mess1_cnt in range(3):
                mess1_cnt += 1
                menu=input("Enter menu name:-")
                mess1_menu.append(str(menu))

        elif name == mess_name2:
            for mess2_cnt in range(3):
                mess2_cnt += 1
                menu=input("Enter menu name:-")
                mess2_menu.append(str(menu))

print("Mess List")
print("1",mess_name1,"\n2",mess_name2)
messname =input("enter mess name:-")
if messname == mess_name1:
    print("\nTodays Menu of:-", mess_name1)
    print(mess1_menu)
elif messname == mess_name2:
    print("\nTodays Menu of:-", mess_name2)
    print(mess2_menu)


