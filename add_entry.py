file_name = "My Chocolates.txt"


def add_choc():
    flag = True   # using flag to break out of while loop
    while flag:
        # taking inputs for chocolate name and quantity

        name = input("Enter chocolate name: ").casefold()
        quantity = input(f"Enter quantity for {name}: ")

        # concatenation of name and quantity in readable format

        choc_data = name + ': ' + quantity + '\n'

        # writing data into file
        # using append mode so no previous data is overwritten

        with open(file_name, 'a') as file:
            file.writelines(choc_data)

        print(f"{quantity} {name} added to inventory successfully!")

        # asking user if they want to add more chocolates or not

        print()

        print("Would you like to add more chocolates? (Y/N) \n")

        while True:
            choice = input('> ').casefold()
            if choice == 'y':
                print()
                break
            elif choice == 'n':
                flag = False
                break
            else:
                print("Please enter a valid input. \n")
