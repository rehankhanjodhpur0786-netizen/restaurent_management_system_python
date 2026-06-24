from app.database.db import Database
import hashlib
import msvcrt  


def masked_input(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""

    while True:
        char = msvcrt.getch()

        
        if char == b'\r':
            print("")
            break

        
        elif char == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        else:
            try:
                password += char.decode("utf-8")
                print("*", end="", flush=True)
            except:
                pass

    return password


class Auth:
    def __init__(self):
        self.db = Database("data/users.json")

    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def signup(self):
        users = self.db.load()

        username = input("Username: ")
        password = masked_input("Password: ")   

        role = input("Are you Admin or Staff? (admin/staff): ").lower()

        if role not in ["admin", "staff"]:
            print("Invalid role! Defaulting to staff")
            role = "staff"

        
        for u in users:
            if u["username"] == username:
                print("User already exists")
                return

        users.append({
            "username": username,
            "password": self.hash_password(password),
            "role": role
        })

        self.db.save(users)
        print("Signup successful")

    
    def signin(self):
        users = self.db.load()

        username = input("Username: ")
        password = masked_input("Password: ")   

        hashed = self.hash_password(password)

        for u in users:
            if u["username"] == username and u["password"] 
                print("Login successful")
                print("Role:", u["role"])

                return {
                    "username": u["username"],
                    "role": u["role"]
                }

        print("Invalid login")
        return None