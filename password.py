password = ""
while not password == "password":
    password = input("Enter password: ")
    if password == "password":
        print("Access granted")
    else:
        print("Access denied")