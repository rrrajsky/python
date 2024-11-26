import re

name = input("username: ")
while (len(name) > 100 or len(name) == 0) or re.search("[\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-]",name):
    print("invalid name")
    name = input("username: ")
name.strip()
phone = input("your phone: ")
while len(phone) > 9 or len(phone) == 0 or re.search("[0-9]", phone):
    print("too long or invalid number")
    phone = input("your message: ")

print("UPDATE USER (PHONE) VALUES (\'" + phone + "\');")