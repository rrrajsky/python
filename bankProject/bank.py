# bank.py

import json
import os
import threading
import logging
from config import DATA_FILE, ACCOUNT_MIN, ACCOUNT_MAX

class Bank:
    """
    Třída, která reprezentuje banku.
    Ukládá informace o účtech (číslo účtu a zůstatek).
    Data jsou chráněna zámkem a při změnách se zapisují do JSON souboru.
    """
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.lock = threading.Lock()
        self.accounts = {}  # {account_number (int): balance (int)}
        self.load_data()

    def load_data(self):
        """ Načte data z perzistentního úložiště. """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    # Klíče jsou uloženy jako řetězce, převedeme je na int
                    self.accounts = {int(k): int(v) for k, v in data.items()}
                    logging.info("Data načtena z '%s'", self.data_file)
            except Exception as e:
                logging.error("Chyba při načítání dat: %s", e)
        else:
            self.accounts = {}

    def save_data(self):
        """ Uloží aktuální stav účtů do souboru. """
        try:
            with open(self.data_file, "w") as f:
                # Převod klíčů na řetězce pro JSON
                json.dump({str(k): v for k, v in self.accounts.items()}, f)
                logging.debug("Data uložena do '%s'", self.data_file)
        except Exception as e:
            logging.error("Chyba při ukládání dat: %s", e)

    def create_account(self):
        """ Vytvoří nový účet s unikátním číslem a počátečním zůstatkem 0. """
        with self.lock:
            for num in range(ACCOUNT_MIN, ACCOUNT_MAX+1):
                if num not in self.accounts:
                    self.accounts[num] = 0
                    self.save_data()
                    logging.info("Vytvořen účet: %d", num)
                    return num
            raise Exception("Žádné volné číslo účtu.")

    def deposit(self, account, amount):
        """ Vloží částku na účet. """
        if amount < 0:
            raise Exception("Částka musí být nezáporná.")
        with self.lock:
            if account in self.accounts:
                self.accounts[account] += amount
                self.save_data()
                logging.info("Vklad %d na účet %d", amount, account)
            else:
                raise Exception("Účet neexistuje.")

    def withdraw(self, account, amount):
        """ Vybere částku z účtu. """
        if amount < 0:
            raise Exception("Částka musí být nezáporná.")
        with self.lock:
            if account in self.accounts:
                if self.accounts[account] >= amount:
                    self.accounts[account] -= amount
                    self.save_data()
                    logging.info("Výběr %d z účtu %d", amount, account)
                else:
                    raise Exception("Není dostatek finančních prostředků.")
            else:
                raise Exception("Účet neexistuje.")

    def get_balance(self, account):
        """ Vrátí zůstatek na účtu. """
        with self.lock:
            if account in self.accounts:
                return self.accounts[account]
            else:
                raise Exception("Účet neexistuje.")

    def remove_account(self, account):
        """ Odstraní účet, pokud je zůstatek 0. """
        with self.lock:
            if account in self.accounts:
                if self.accounts[account] == 0:
                    del self.accounts[account]
                    self.save_data()
                    logging.info("Účet %d odstraněn", account)
                else:
                    raise Exception("Nelze smazat bankovní účet na kterém jsou finance.")
            else:
                raise Exception("Účet neexistuje.")

    def total_amount(self):
        """ Vrátí celkovou částku ve všech účtech. """
        with self.lock:
            return sum(self.accounts.values())

    def count_clients(self):
        """ Vrátí počet účtů (klientů). """
        with self.lock:
            return len(self.accounts)
