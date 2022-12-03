login = input("Login: ")
password = input("Password: ")
password_length = len(password)
hidden_password = password_length * "*"
print(f"{login}, your password {hidden_password} is {password_length} letters long" )