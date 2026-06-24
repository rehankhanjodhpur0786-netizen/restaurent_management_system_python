class MenuUI:

    def auth_menu(self):
        print("\n===== AUTH MENU =====")
        print("1. Sign Up")
        print("2. Sign In")
        print("0. Exit")
        return input("Enter choice: ")

    def main_menu(self):
        print("\n===== MAIN MENU =====")
        print("1. Order System")
        print("2. Show Menu")
        print("3. Billing")
        print("4. Table Booking")
        print("0. Exit")
        return input("Enter choice: ")

    def order_menu(self):
        print("\n===== ORDER MENU =====")
        print("1. Take Order")
        print("2. Add Order")
        print("3. Show Orders")
        print("4. Delete Order")
        print("0. Back")
        return input("Enter choice: ")