import re

def password_policy_check(username, password):
    if len(password) < 10 or not re.search("[a-z]",password) or not re.search("[A-Z]",password) or not re.search("[0-9]",password) or not re.search("[\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-]",password) or password == username:
        return "password invalid!"
    else:
        for i in range(4, len(username) + 1):
            if username[:i] in password:
                return "password invalid!"
        return "password valid!"


username = input("Enter username: ")
password = input("Enter password: ")

print(password_policy_check(username,password))

