List = []

while True:
    choice = input("1) Add Item\n2) Remove Item\n3) View List\n4) Exit\nChoice: ")


    match choice:
        case "1":
            add = input("Please add an Item: ")
            List.append(add)
            print(f"You succesfully added {add} to the list!")
        case "2":
            if not List:
                print("List is empty. Nothing to remove...")
            else:
                for idx, item in enumerate(List):
                    print(f"{idx}: {item}")
                try:
                    remove = int(input("Please choose an index to remove: "))
                    print(f"You have succesfully removed {List [remove]}")
                    List.pop(remove)
                except(ValueError, IndexError):
                    print("Invalid Index!")
        case "3":
            if not List:
                print("List is empty...")
            else:
                print("Showing List...")
                for idx, item in enumerate(List):
                    print(f"{idx}: {item}")
        case "4":
            print("Exiting...")
            break
        case _:
            print("Invalid choice.")

    print("\n")

        
