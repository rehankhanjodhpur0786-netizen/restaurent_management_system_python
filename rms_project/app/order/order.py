from app.database.db import Database


class Order:
    def __init__(self):
        self.order_db = Database("data/orders.json")
        self.menu_db = Database("data/menu.json")

    def show_menu(self):
        menu = self.menu_db.load()

        print("\n===== MENU =====")

        for i, item in enumerate(menu, 1):
            print(f"{i}. {item['name']} ({item['type']}) - {item['price']}")

        return menu

    def take_order(self, user):
        menu = self.menu_db.load()
        orders = self.order_db.load()

        self.show_menu()

        try:
            choice = int(input("\nEnter item number: "))
        except:
            print("Invalid input")
            return

        if choice < 1 or choice > len(menu):
            print("Invalid choice")
            return

        item = menu[choice - 1]

        order_data = {
            "username": user["username"],
            "role": user["role"],
            "item": item
        }

        orders.append(order_data)
        self.order_db.save(orders)

        print(f"{item['name']} ordered successfully")

    def show_items(self):
        orders = self.order_db.load()

        if not orders:
            print("No orders found")
            return

        print("\nCURRENT ORDERS:")

        for i, o in enumerate(orders, 1):
            item = o.get("item", {})
            print(f"{i}. {item.get('name')} - {item.get('price')} ({o.get('username')})")

    def delete_item(self):
        orders = self.order_db.load()

        name = input("Enter item name to delete: ")

        orders = [o for o in orders if o.get("item", {}).get("name") != name]

        self.order_db.save(orders)
        print("Deleted")