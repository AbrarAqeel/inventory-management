from add_entry import add_choc
from print_entry import print_choc
from update_entry import update_choc
from search_entry import search_choc
from delete_entry import del_choc

print()

if __name__ == '__main__':
    print("\t Welcome to my Chocolate Inventory! \n")

    flag = True
    while flag:
        print()
        print("Would you like to: \n \n"
              "1. Add New Entry. \n"
              "2. Update Existing Entry. \n"
              "3. Search Entry. \n"
              "4. Print Entire Inventory. \n"
              "5. Delete Entry. \n"
              "0. Exit Program. \n")
        choice = input('> ')
        print()
        if choice == '1':
            add_choc()
        elif choice == '2':
            update_choc()
        elif choice == '3':
            search_choc()
        elif choice == '4':
            print_choc()
        elif choice == '5':
            del_choc()
        elif choice == '0':
            print("Program Terminated. \n  \n"
                  "\t Thank you for using the Chocolate Inventory System!")
            flag = False
        else:
            print("Please enter a valid input. \n")
