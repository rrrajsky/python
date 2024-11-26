# H

import re

def clean_input(text): # function for cleaning inputs
    text = re.sub(r'<script.*?>.*?</script>', '', text) # deletes everything within <script>
    text = re.sub(r'<.*?>', '', text) # deletes <>
    text = re.sub(r'\\.*?', '', text)  # should delete \
    return re.sub(r'[^\w\s.,áéíóúýčďěňřšťžůÁÉÍÓÚÝČĎĚŇŘŠŤŽŮ\-+@/]', '', text) # deletes other special symbols

def build_html_address(street, street_number, city, zip):
    clean_street = clean_input(street)
    clean_street_number = clean_input(street_number)
    clean_city = clean_input(city)
    clean_zip = clean_input(zip)
    # cleans every input and returns those
    return "<address>"+clean_street+" "+clean_street_number+"<br/>"+clean_city+"</br>"+clean_zip+"</address>"

def build_html_link(url, label):
    clean_url = clean_input(url)
    clean_label = clean_input(label)
    # cleans every input and returns those
    return "<a href=\""+clean_url+"\">"+clean_label+"</a>"

def build_html_list(monthly_payments):
    xml = "<ul>\n"
    for payment in monthly_payments:
        clean_payment_what = clean_input(payment["what"])
        clean_payment_amount = clean_input(str(payment["amount"]))
        clean_payment_account_number = clean_input(payment["account_number"])
        # should clean every part of each monthly payment and inserts them into xml output
        xml += " <li>"+clean_payment_what+" : "+str(clean_payment_amount)+" EUR to "+clean_payment_account_number+"</li>\n"
    xml += "</ul>\n"
    return xml # returns said xml

print(build_html_address("Ječná","30","Praha","12000"))
print(build_html_link("https://spsejecna.cz","škola Ječná"))
print(build_html_list([
    {"what":"netflix", "account_number" : "0500021502/0800","amount":130, },
    {"what":"o2", "account_number" : "1500023322/0600","amount":1450, }
]))

print(build_html_address("Ječná","30","Praha<script>alert('Hacked!');</script>","12000"))
print(build_html_link("https://spsejecna.cz","škola Ječná</a><img src=\"\" width=\"100\" height=\"200\" alt=\"Hacked logo\"/><a href=\"\">"))
print(build_html_list([
    {"what": "Netflix", "account_number": "0500021502/0800", "amount": 13, },
    {"what": "O2", "account_number": "1500023322/0600</li>\n <li>Hacker : 13 EUR to 8870021522/0300", "amount": 145, }
]))

