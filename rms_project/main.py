from app.auth.auth import Auth
from app.order.order import Order
from app.billing.billing import Billing
from app.table_booking.booking import Booking
from app.menu.menu import MenuUI

auth = Auth()
order = Order()
billing = Billing()
booking = Booking()
menu = MenuUI()


def auth_flow():
    while True:
        choice = menu.auth_menu()

        if choice == "1":
            auth.signup()

        elif choice == "2":
            user = auth.signin()
            if user:
                return user

        elif choice == "0":
            return None


def main():
    user = auth_flow()

    if not user:
        print("Thank you")
        return

    print(f"\nWelcome {user['username']} ({user['role']})")

    while True:
        choice = menu.main_menu()

        
        if choice == "1":
            while True:
                c = menu.order_menu()

                if c == "1":
                    order.take_order(user)

                elif c == "2":
                    order.take_order(user)

                elif c == "3":
                    order.show_items()

                elif c == "4":
                    order.delete_item()

                elif c == "0":
                    break

        
        elif choice == "2":
            order.show_menu()

        
        elif choice == "3":
            billing.generate_bill(user)

        
        elif choice == "4":
            booking.book_table()

        
        elif choice == "0":
            print("thank you and please code tomorrow")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()