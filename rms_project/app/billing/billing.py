from app.database.db import Database


class Billing:
    def __init__(self):
        self.db = Database("data/orders.json")

    def generate_bill(self, user):
        orders = self.db.load()

        
        user_orders = [
            o for o in orders if o.get("username") == user["username"]
        ]

        if not user_orders:
            print("No orders found")
            return

        print("\n===== BILL =====")

        total = 0

        for i, o in enumerate(user_orders, 1):
            item = o.get("item", {})
            name = item.get("name", "Unknown")
            price = item.get("price", 0)

            print(f"{i}. {name} - {price}")
            total += price

        print("-------------------")
        print("TOTAL BILL:", total)