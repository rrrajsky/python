import re

# Napište metodu, která bude součástí diskusního fóra na webu.
# Na vstupu přijme dva argumenty: nickname autora,
# text autora a vrátí SQL příkaz pro vložení příspěvku do
# MySQL databázové tabulky, která je definována takto:
#
# CREATE TABLE PRISPEVEK (
#
#   ID INT NOT NULL AUTO_INCREMENT,
#
#   AUTHOR VARCHAR(100) NOT NULL,

#   TEXT TINYTEXT NOT NULL,
#
#   PRIMARY KEY (ID));
# ----------------------------------------------------------------------
# Opravte metodu z úlohy 7.1. aby nebylo možné provést SQL Injection.

name = input("username: ")
while (len(name) > 100 or len(name) == 0) or re.search("[\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-]",name):
    print("invalid name")
    name = input("username: ")
name.strip()
text = input("your message: ")
while len(text) > 255 or len(text) == 0 or re.search("[\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-]",text):
    print("too long")
    text = input("your message: ")

print("INSERT INTO PRISPEVEK (AUTHOR, TEXT) VALUES (\'"+ name + "\', \'" + text + "\');")
