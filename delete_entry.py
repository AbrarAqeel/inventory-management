from add_entry import file_name


def del_choc():
    removed = False   # to check if data exists or not
    flag = True
    while flag:
        name = input("Enter chocolate name: ").casefold()
        search_name = name + ':'

        # reading data from file

        with open(file_name, 'r') as file:
            data = file.readlines()

        # converting into list and deleting value

        for line in data:
            line1 = line.strip('\n')  # eliminating new line
            line1 = line.split()  # converting into lists

            if line1[0] == search_name:
                data.remove(line)
                removed = True
                print()
                print(f"{name} has been deleted successfully.")

        if not removed:
            print(f"{name} does not exists.")

        with open(file_name, 'w') as file:
            file.writelines(data)

        print("Do you want to delete more entries? (Y/N)")
        choice = input("> ").casefold()
        if choice == 'y':
            continue
        elif choice == 'n':
            flag = False
        else:
            print("Please enter a valid input.")
