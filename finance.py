"""
Finance Branch
--------------
Handles monetary storage, deposits, withdrawals, cash drawer audits,
and bank processing.
"""


class Finance:
    """Base financial account managing balance and core money operations."""

    def __init__(self, initial_balance: float = 0.0):
        # Store balance as a float to handle currency values
        self.balance = float(initial_balance)

    def add_money(self, amount: float) -> bool:
        """Deposits a positive amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Added ${amount:.2f} to {self.__class__.__name__}. Current Balance: ${self.balance:.2f}")
            return True
        return False

    def remove_money(self, amount: float) -> bool:
        """Deducts a positive amount if sufficient funds exist."""
        if amount <= 0:
            print("Amount must be positive.")
            return False
        if amount > self.balance:
            print(f"Insufficient funds in {self.__class__.__name__}!")
            return False

        self.balance -= amount
        print(f"Removed ${amount:.2f} from {self.__class__.__name__}. Remaining Balance: ${self.balance:.2f}")
        return True


class Bank(Finance):
    """Electronic banking system tracking total card processing sales."""

    def __init__(self, initial_balance: float = 0.0):
        super().__init__(initial_balance)
        self.total_card_sales = 0.0

    def process_card_deposit(self, total_amount: float) -> None:
        """Increments card sales metrics and credits the bank account balance."""
        self.total_card_sales += total_amount
        self.add_money(total_amount)


class Drawer(Finance):
    """Physical cash drawer with threshold audits and change availability checks."""

    def __init__(self, initial_balance: float = 0.0, min_float: float = 50.0):
        super().__init__(initial_balance)
        self.min_float = min_float  # Minimum cash threshold required to operate safely

    def can_give_change(self, change_amount: float) -> bool:
        """Verifies if the cash drawer holds enough float to provide change."""
        if change_amount > self.balance:
            print(f"Drawer Warning: Insufficient cash float! Required: ${change_amount:.2f}, Available: ${self.balance:.2f}")
            return False
        return True

    def audit_drawer(self) -> None:
        """Warns the operator if cash falls below the safe operating float."""
        if self.balance < self.min_float:
            print(f"Alert: Drawer cash is low (${self.balance:.2f}). Needs cash refill.")
        else:
            print(f"Drawer Status: Healthy (${self.balance:.2f} available)")
