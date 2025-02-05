# request_handler.py

import socket
import socketserver
import logging
from bank import Bank
from config import get_local_ip, DEFAULT_TIMEOUT, DEFAULT_PORT

# Vytvoříme globální instanci banky, kterou využijeme pro všechny požadavky.
bank = Bank()

def proxy_command(command_line, remote_ip):
    """
    Přepošle daný příkaz na vzdálený uzel (s IP remote_ip) a vrátí jeho odpověď.
    Používá předpokládaný port DEFAULT_PORT z config.py.
    """
    try:
        with socket.create_connection((remote_ip, DEFAULT_PORT), timeout=DEFAULT_TIMEOUT) as sock:
            sock.sendall((command_line + "\n").encode("utf-8"))
            # Přečteme odpověď jako jeden řádek
            sock_file = sock.makefile("r", encoding="utf-8")
            response = sock_file.readline().strip()
            return response
    except Exception as e:
        return f"ER Chyba při proxy komunikaci: {str(e)}"

class BankRequestHandler(socketserver.StreamRequestHandler):
    """
    Obsluha příchozích TCP spojení.
    Každé spojení čeká v cyklu na příchozí příkazy, dokud klient sám nespadne či neukončí spojení.
    """
    def handle(self):
        self.request.settimeout(DEFAULT_TIMEOUT)
        client_ip, client_port = self.client_address
        logging.info("Připojen klient %s:%s", client_ip, client_port)
        
        while True:
            try:
                # Přečteme jeden řádek (UTF-8, odřádkování)
                line = self.rfile.readline().decode("utf-8").strip()
                # Pokud se klient odpojí, readline vrátí prázdný řetězec.
                if not line:
                    logging.info("Klient %s:%s ukončil spojení.", client_ip, client_port)
                    break

                logging.debug("Přijat příkaz: %s", line)
                response = self.process_command(line)
                # Odešleme odpověď s ukončovacím znakem nového řádku
                self.wfile.write((response + "\n").encode("utf-8"))
                logging.debug("Odeslána odpověď: %s", response)
            except socket.timeout:
                logging.error("Timeout klienta %s:%s", client_ip, client_port)
                break  # Ukončíme obsluhu při vypršení timeoutu
            except Exception as e:
                logging.exception("Chyba při obsluze klienta: %s", e)
                break  # Ukončíme spojení v případě neočekávané chyby

    def process_command(self, command_line):
        """
        Rozpozná a vykoná příkaz podle protokolu.
        Vrací řetězec odpovědi.
        """
        parts = command_line.split()
        if not parts:
            return "ER Prázdný příkaz."

        cmd = parts[0].upper()  # příkaz velkými písmeny
        local_ip = get_local_ip()

        try:
            if cmd == "BC":
                # Vrátí bankovní kód (IP adresu)
                return f"BC {local_ip}"

            elif cmd == "AC":
                # Vytvoří nový účet
                acc_num = bank.create_account()
                return f"AC {acc_num}/{local_ip}"

            elif cmd == "AD":
                # Vklad na účet, syntax: AD <account>/<ip> <amount>
                if len(parts) != 3:
                    raise Exception("Špatný formát příkazu AD.")
                account_field = parts[1]
                amount_field = parts[2]
                try:
                    acc_str, ip_part = account_field.split("/")
                    account = int(acc_str)
                    amount = int(amount_field)
                except Exception:
                    raise Exception("Číslo bankovního účtu a částka není ve správném formátu.")
                # Pokud je IP v příkazu odlišná, předáme příkaz jako proxy
                if ip_part != local_ip:
                    return proxy_command(command_line, ip_part)
                else:
                    bank.deposit(account, amount)
                    return "AD"

            elif cmd == "AW":
                # Výběr z účtu, syntax: AW <account>/<ip> <amount>
                if len(parts) != 3:
                    raise Exception("Špatný formát příkazu AW.")
                account_field = parts[1]
                amount_field = parts[2]
                try:
                    acc_str, ip_part = account_field.split("/")
                    account = int(acc_str)
                    amount = int(amount_field)
                except Exception:
                    raise Exception("Číslo bankovního účtu a částka není ve správném formátu.")
                if ip_part != local_ip:
                    return proxy_command(command_line, ip_part)
                else:
                    bank.withdraw(account, amount)
                    return "AW"

            elif cmd == "AB":
                # Zůstatek na účtu, syntax: AB <account>/<ip>
                if len(parts) != 2:
                    raise Exception("Špatný formát příkazu AB.")
                account_field = parts[1]
                try:
                    acc_str, ip_part = account_field.split("/")
                    account = int(acc_str)
                except Exception:
                    raise Exception("Formát čísla účtu není správný.")
                if ip_part != local_ip:
                    return proxy_command(command_line, ip_part)
                else:
                    balance = bank.get_balance(account)
                    return f"AB {balance}"

            elif cmd == "AR":
                # Smazání účtu, syntax: AR <account>/<ip>
                if len(parts) != 2:
                    raise Exception("Špatný formát příkazu AR.")
                account_field = parts[1]
                try:
                    acc_str, ip_part = account_field.split("/")
                    account = int(acc_str)
                except Exception:
                    raise Exception("Formát čísla účtu není správný.")
                # Příkaz AR se proxy nepřenáší – předpokládáme, že účet se maže lokálně
                if ip_part != local_ip:
                    raise Exception("Příkaz AR lze provést pouze lokálně.")
                bank.remove_account(account)
                return "AR"

            elif cmd == "BA":
                # Celková částka ve všech účtech
                if len(parts) != 1:
                    raise Exception("Špatný formát příkazu BA.")
                return f"BA {bank.total_amount()}"

            elif cmd == "BN":
                # Počet klientů (účtů)
                if len(parts) != 1:
                    raise Exception("Špatný formát příkazu BN.")
                return f"BN {bank.count_clients()}"

            else:
                return "ER Nepodporovaný příkaz."

        except Exception as e:
            # Vrací chybu ve formátu "ER <message>"
            return f"ER {str(e)}"
