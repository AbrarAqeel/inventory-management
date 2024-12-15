from add_entry import file_name


def print_choc():
    # reading data from file

    with open(file_name, 'r') as file:
        data = file.read()

    print("\t My Chocolate Inventory =D \n")
    print(data)   # printing data
    print()

    # waiting for user's input to continue

    flag = True
    while flag:
        print("Press any key to continue...", end='')
        input()
        flag = False
