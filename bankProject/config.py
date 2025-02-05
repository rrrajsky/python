# config.py

import socket

# Cesta k souboru s perzistentními daty
DATA_FILE = "bank_data.json"

# Rozsah čísel účtů
ACCOUNT_MIN = 10000
ACCOUNT_MAX = 99999

# Timeout v sekundách (výchozí)
DEFAULT_TIMEOUT = 60

# Výchozí port, který se použije při proxy komunikaci.
# Pozn.: Lokální server může běžet na jiném portu, avšak pro účely proxy předpokládáme, že uzly používají jednotný port.
DEFAULT_PORT = 65530

def get_local_ip():
    """
    Získá IP adresu lokálního rozhraní.
    Tato metoda se pokusí vytvořit spojení do internetu a pak získat svou lokální adresu.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Nepotřebujeme skutečně odeslat data
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            return ip
    except Exception:
        return "127.0.0.1"
