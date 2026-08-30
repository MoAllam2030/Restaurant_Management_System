"""
Payment Branch
--------------
Handles transaction calculations (taxes, tips, totals) and processes
customer payments via cash or card.
"""

# Import financial accounts from the finance module
from finance import Bank, Drawer


class Payment:
    """Base payment processor for calculating taxes, tips, and totals."""

    def __init__(self, amount_needed: float, amount_paid: float = 0.0):
        self.amount_needed = float(amount_needed)  # Base item / bill price
        self.amount_paid = float(amount_paid)      # Amount provided by customer

    def tax(self) -> float:
        """Calculates a flat 10% sales tax on the base amount."""
        return self.amount_needed * 0.10

    def tipping(self, percent_choice: int) -> float:
        """Maps tip selection (1-4) to corresponding percentage."""
        tip_percentages = {1: 0.05, 2: 0.10, 3: 0.15, 4: 0.20}
        percent = tip_percentages.get(percent_choice, 0.0)
        return self.amount_needed * percent

    def ask_for_tip(self) -> float:
        """Prompts user for tipping options with input validation."""
        is_tip = input("Would you like to tip? (yes / no): ").strip().lower()
        if is_tip in ["yes", "y"]:
            print("How much would you like to tip?")
            print("1- 5%    2- 10%\n3- 15%   4- 20%")
            try:
                percent = int(input("Choice: "))
                return self.tipping(percent)
            except ValueError:
                print("Invalid choice. No tip applied.")
        return 0.0

    def calculate_total(self) -> float:
        """Combines base price, tax, and tip into final amount due."""
        tip = self.ask_for_tip()
        return self.amount_needed + self.tax() + tip

    def change(self, total_due: float) -> float:
        """Calculates difference between paid amount and total due."""
        return self.amount_paid - total_due


class CashPayment(Payment):
    """Processes cash transactions and updates physical cash drawer."""

    def process_cash(self, drawer: Drawer) -> bool:
        """Performs cash validation, checks drawer balance, updates float, and returns change."""
        total_due = self.calculate_total()
        print(f"Total Due (with tax & tip): ${total_due:.2f}")

        # Capture customer cash input safely
        try:
            self.amount_paid = float(input("Enter cash presented by customer: "))
        except ValueError:
            print("Invalid input for cash amount.")
            return False

        change_due = self.change(total_due)

        # Ensure customer provided enough cash
        if change_due < 0:
            print(f"Not enough cash! Short by ${abs(change_due):.2f}")
            return False

        # Pre-check drawer capacity BEFORE committing transaction
        if not drawer.can_give_change(change_due):
            return False

        # Execute cash flow
        drawer.add_money(self.amount_paid)
        if change_due > 0:
            drawer.remove_money(change_due)
            print(f"Change returned: ${change_due:.2f}")

        # Post-transaction audit
        drawer.audit_drawer()
        return True


class CardPayment(Payment):
    """Processes electronic card payments and routes funds to bank account."""

    def process_card(self, bank: Bank) -> bool:
        """Calculates balance and deposits total straight into bank account."""
        total_due = self.calculate_total()
        print(f"Total Due (with tax & tip): ${total_due:.2f}")
        
        # Set amount paid to exact due amount for card transactions
        self.amount_paid = total_due
        
        # Deposit directly into bank instance
        bank.process_card_deposit(total_due)
        return True
