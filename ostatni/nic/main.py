import re

def sanitize_html_input(text):
    # Odstranění celých bloků scriptu a všech nebezpečných HTML značek
    # Odstraní jakýkoli obsah uvnitř značek <script>...</script>
    text = re.sub(r'<script.*?>.*?</script>', '', text)
    # Odstraní jakékoliv HTML značky (cokoliv mezi < >)
    text = re.sub(r'<.*?>', '', text)
    # Povolení pouze základních bezpečných znaků
    return re.sub(r'[^\w\s.,:;áéíóúýčďěňřšťžÁÉÍÓÚÝČĎĚŇŘŠŤŽ\-+@/]', '', text)

# Funkce pro odstranění potenciálně nebezpečných znaků z XML
def sanitize_xml_input(text):
    # Odstraní jakýkoli obsah uvnitř značek <script>...</script>
    text = re.sub(r'<script.*?>.*?</script>', '', text)
    # Odstraní jakékoli XML značky (cokoliv mezi < >)
    text = re.sub(r'<.*?>', '', text)
    # Povolení pouze základních bezpečných znaků (písmena, čísla, interpunkce)
    return re.sub(r'[^\w\s.,:;áéíóúýčďěňřšťžÁÉÍÓÚÝČĎĚŇŘŠŤŽ\-+@]', '', text)

def build_html_contact_item(name, phone):
    # Sanitace vstupů pomocí regexu
    safe_name = sanitize_html_input(name)
    safe_phone = sanitize_html_input(phone)
    return f'<div class="contact_item"><h2>{safe_name}</h2><p>Phone: {safe_phone}</p></div>'

def build_html_img(path, width, height, description=""):
    # Sanitace cesty a popisku pomocí regexu
    safe_path = sanitize_html_input(path)
    safe_description = sanitize_html_input(description)
    return f'<img src="{safe_path}" alt="{safe_description}" width="{width}" height="{height}">'

def build_xml_from_money_transactions(money_transactions):
    xml = "<money_transactions>\n"
    for transaction in money_transactions:
        # Sanitace vstupů pomocí regexu
        safe_account_number = sanitize_xml_input(transaction["account_number"])
        safe_amount = sanitize_xml_input(str(transaction["amount"]))
        safe_message = sanitize_xml_input(transaction["message"])
        xml += f" <transaction>\n  <account_number>{safe_account_number}</account_number>\n"
        xml += f"  <amount>{safe_amount}</amount>\n"
        xml += f"  <message>{safe_message}</message>\n </transaction>\n"
    xml += "</money_transactions>\n"
    return xml

# Test cases
# print(build_html_contact_item("Ing. Jan Novák", "+420 606321423"))
# print(build_html_img("/img/obrazek.jpg", 80, 40, "Logo firmy"))
# print(build_xml_from_money_transactions([
#     {"account_number": "0500021502/0800", "amount": 1300, "message": "Platba za obědy Jan Novák"},
#     {"account_number": "1500023322/0600", "amount": 1450, "message": "Obědy Petr Novák"}
# ]))

# Demonstrace prevence proti HTML a XML injection
print(build_html_contact_item("Ing. Jan Novák", "+420 606321423</p></div><script>alert('Hacked!');</script><p><div>"))
print(build_html_img("/img/obrazek.jpg", 80, 40, '"/><img src="" width="100" height="200" alt="Hacked logo'))
print(build_xml_from_money_transactions([
    {"account_number": "0500021502/0800", "amount": 1300, "message": "Platba za obědy Jan Novák"},
    {"account_number": "1500023322/0600", "amount": 1450, "message": "Obědy Petr Novák</message>\n </transaction>\n <transaction>\n  <account_number>0700098720/0100</account_number>\n  <amount>1000000</amount>\n"}
]))
