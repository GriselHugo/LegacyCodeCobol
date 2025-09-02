# banking_system.py

class DataProgram:
    """Simule la gestion du stockage du solde (comme data.cob)."""
    def __init__(self, initial_balance=1000.00):
        self._storage_balance = initial_balance

    def read(self):
        """Retourne le solde actuel."""
        return self._storage_balance

    def write(self, new_balance):
        """Met à jour le solde."""
        self._storage_balance = new_balance


class Operations:
    """Gère les opérations de crédit, débit et affichage du solde."""
    def __init__(self, data_program):
        self.data_program = data_program

    def total(self):
        balance = self.data_program.read()
        print(f"Current balance: {balance:.2f}")

    def credit(self):
        try:
            amount = float(input("Enter credit amount: "))
        except ValueError:
            print("Invalid amount.")
            return
        balance = self.data_program.read()
        balance += amount
        self.data_program.write(balance)
        print(f"Amount credited. New balance: {balance:.2f}")

    def debit(self):
        try:
            amount = float(input("Enter debit amount: "))
        except ValueError:
            print("Invalid amount.")
            return
        balance = self.data_program.read()
        if balance >= amount:
            balance -= amount
            self.data_program.write(balance)
            print(f"Amount debited. New balance: {balance:.2f}")
        else:
            print("Insufficient funds for this debit.")


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
