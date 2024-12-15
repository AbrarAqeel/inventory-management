from add_entry import file_name


def search_choc():
    found = False  # to check if data exists or not
    flag = True
    while flag:
        name = input("Enter chocolate name: ").casefold()
        search_name = name + ':'

        # reading data from file

        with open(file_name, 'r') as file:
            data = file.readlines()

        # converting into list

        for line in data:
            line1 = line.strip('\n')  # eliminating new line
            line1 = line.split()  # converting into lists

            if line1[0] == search_name:
                found = True
                print()
                print(f"You have {line1[1]} {name} in your inventory.")

        if not found:
            print(f"{name} does not exists.")

        print("Do you want to search more entries? (Y/N)")
        choice = input("> ").casefold()
        if choice == 'y':
            continue
        elif choice == 'n':
            flag = False
        else:
            print("Please enter a valid input.")
