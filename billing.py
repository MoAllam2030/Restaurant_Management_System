class PaymentMethod:  # Base class (Inheritance)
    def pay(self, amount):
        pass

class CashPayment(PaymentMethod): # Polymorphism
    def pay(self, amount):
        print(f"💵 Received ${amount:.2f} in Cash.")
        return True

class CardPayment(PaymentMethod): # Polymorphism
    def pay(self, amount):
        print(f"💳 Card approved for ${amount:.2f}.")
        return True

class BillingSystem:
    def process_bill(self, order, payment_method):
        # 7. Bill Calculation
        subtotal = sum(item.price for item in order.items)
        tax = subtotal * 0.10
        total = subtotal + tax

        # 9. Receipt Generation
        print(f"\n--- 🧾 RECEIPT: TABLE {order.table.table_number} ---")
        for item in order.items:
            print(f"  {item.name}: ${item.price:.2f}")
        print(f"  Tax: ${tax:.2f}")
        print(f"  TOTAL: ${total:.2f}")
        print("------------------------")

        # 8. Process Payment
        return payment_method.pay(total), total