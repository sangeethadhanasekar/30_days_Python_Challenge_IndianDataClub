'''🎯 Challenge
- Create an inventory system tracking items and quantities with a dictionary'''

inventory={"paper":10, "pencil":20}

def view_inventory():
    print("\n------items in inventory-----")
    for i,j in inventory.items():
        print(i,":",j)
    print("------------------")


def add_item():
    print("\n------Add item-----")
    item=input("Enter the item name:")
    inventory[item]=input("Enter the quantity of item: ")
    print("\n",item,":",inventory[item]," added to inventory") 
    print("---------------------")

def update_item():
    view_inventory()
    print("\n------update item-----")
    item=input("Enter the item to be updated: ")
    inventory[item]= input("Enter the updated quantity:")
    print("\n",item,":",inventory[item]," updated to inventory")
    print("---------------------")

def delete_item():
    view_inventory()
    print("\n------delete item-----")
    item= input("Enter the item to be deleted: ")
    del inventory[item]
    print("\n", item, " is deleted from inventory")
    print("---------------------")

def exit():
    print("\n------------------")
    print("\nInventory system is exited!!")
    print("\n---------------------")
    


print("\nInventory system tracking")

loop=True
while (loop):
        try:
            option= int(input(" \n 1.view inventory \n 2.add item to inventory \n 3.update quantities of items \n 4.delete an item \n 5.Exit  \n Enter the option:  "))
            if option == 1:
                view_inventory()
                
            elif option == 2:
                view_inventory()
                add_item()
                
            elif option == 3:
                view_inventory()
                update_item()
                
            elif option == 4:
                view_inventory()
                delete_item()
                
            elif option == 5:
                exit()
                loop=False 
            else: print("\ninvalid response, Choose the correct option!")
        except ValueError: print("\n Warning! the option should be an number(integer)\n")
    