from app.database.db import Database


class Booking:
    def __init__(self):
        self.db = Database("data/bookings.json")

    def book_table(self):
        data = self.db.load()

        name = input("Customer name: ")
        table_no = input("Table number: ")

        data.append({
            "name": name,
            "table": table_no
        })

        self.db.save(data)
        print("Table booked successfully")

    def show_bookings(self):
        print(self.db.load())