
users = {
    "admin": "admin123",
    "john": "john@123",
    "alice": "alice2024"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username] == password:
        print("Login Successful!")
    else:
        print("Incorrect Password ")
else:
    print("Username not found ")