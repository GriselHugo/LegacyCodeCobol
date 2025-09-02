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
