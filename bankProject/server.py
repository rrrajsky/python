# server.py
import logging_setup
import socketserver
import argparse
import logging
from request_handler import BankRequestHandler
from config import DEFAULT_TIMEOUT, get_local_ip

# Konfigurace logování
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s')

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Umožňuje znovupoužití adresy (bez čekání na timeout)
    allow_reuse_address = True

def parse_arguments():
    parser = argparse.ArgumentParser(description="P2P Bankovní uzel - verze μ (mí)")
    parser.add_argument(
        "--port", type=int, default=65530,
        help="Port, na kterém bude uzel naslouchat (65525-65535). Výchozí: 65530"
    )
    parser.add_argument(
        "--timeout", type=int, default=DEFAULT_TIMEOUT,
        help="Timeout pro odpovědi v sekundách (výchozí 5 sekund)."
    )
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Kontrola, zda je port v povoleném rozsahu
    if args.port < 65525 or args.port > 65535:
        logging.error("Port musí být v rozsahu 65525 až 65535.")
        return

    # Aktualizace globálního timeoutu (případně jej předáme handleru)
    # V našem příkladu se používá hodnota z config.py, proto lze tuto hodnotu případně i přepsat
    # například: import config; config.DEFAULT_TIMEOUT = args.timeout

    host = ""  # nasloucháme na všech rozhraních
    server_address = (host, args.port)
    logging.info("Spouštím bankovní uzel na portu %d s timeoutem %d s.", args.port, args.timeout)
    try:
        with ThreadedTCPServer(server_address, BankRequestHandler) as server:
            logging.info("IP adresa uzlu: %s", get_local_ip())
            server.serve_forever()
    except Exception as e:
        logging.error("Chyba serveru: %s", e)

if __name__ == "__main__":
    main()
