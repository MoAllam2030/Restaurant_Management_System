from entity import Table, Order
from inventory_menu import RestaurantData
from kitchen import KitchenSystem
from billing import BillingSystem, CardPayment

class RestaurantApp:
    def __init__(self):
        # Initializing the team's modules
        self.data = RestaurantData()
        self.kitchen = KitchenSystem()
        self.billing = BillingSystem()
        
        # 2. Table Management & 10. Sales Tracking
        self.tables = [Table(1), Table(2), Table(3)]
        self.total_sales = 0

    def run_simulation(self):
        print("=== 🍽️ RESTAURANT OPENED ===\n")
        
        # Customer sits at Table 1
        table = self.tables[0]
        table.is_occupied = True
        
        # 3. Order Taking
        current_order = Order(table)
        pizza = self.data.get_menu_item("Pizza")
        
        if self.data.consume_ingredients(pizza):
            current_order.add_item(pizza)
            
            # Send to kitchen
            self.kitchen.receive_order(current_order)
            
            # Kitchen finishes food
            self.kitchen.finish_cooking()
            current_order.status = "Served"
            
            # Customer pays
            success, amount_paid = self.billing.process_bill(current_order, CardPayment())
            
            if success:
                self.total_sales += amount_paid
                table.is_occupied = False
                print(f"\n✅ Transaction complete. Table {table.table_number} is free.")
                print(f"📈 Total Daily Sales: ${self.total_sales:.2f}")

if __name__ == "__main__":
    app = RestaurantApp()
    app.run_simulation()
