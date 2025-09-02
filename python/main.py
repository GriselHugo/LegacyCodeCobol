from data import DataProgram
from operations import Operations


def main():
    data = DataProgram()
    ops = Operations(data)

    continue_flag = True
    while continue_flag:
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            ops.total()
        elif choice == "2":
            ops.credit()
        elif choice == "3":
            ops.debit()
        elif choice == "4":
            continue_flag = False
        else:
            print("Invalid choice, please select 1-4.")

    print("Exiting the program. Goodbye!")


if __name__ == "__main__":
    main()
