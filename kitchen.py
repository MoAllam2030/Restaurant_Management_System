class KitchenSystem:
    def __init__(self):
        # 5. Kitchen Routing
        self.order_queue = []

    def receive_order(self, order):
        # 6. Order Status Updates
        order.status = "Preparing"
        self.order_queue.append(order)
        print(f"👨‍🍳 Kitchen received order for Table {order.table.table_number}")

    def finish_cooking(self):
        if self.order_queue:
            finished_order = self.order_queue.pop(0)
            finished_order.status = "Ready to Serve"
            print(f"🔔 Order for Table {finished_order.table.table_number} is ready!")
            return finished_order
        return None