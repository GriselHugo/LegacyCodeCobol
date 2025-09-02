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
