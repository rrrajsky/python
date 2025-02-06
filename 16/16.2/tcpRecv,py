import socket
import random
from datetime import datetime

# Command interface
class Command:
    def execute(self) -> str:
        pass

# Concrete commands
class QuoteCommand(Command):
    quotes = [
        "Život je jako kniha. Hlupáci v ní listují, moudří ji čtou pozorně.",
        "Jediným způsobem, jak dosáhnout nemožného, je uvěřit, že je možné.",
        "Úspěch je schopnost jít od neúspěchu k neúspěchu bez ztráty nadšení.",
    ]
    
    def execute(self):
        return random.choice(self.quotes)

class DateCommand(Command):
    def execute(self):
        return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class HelpCommand(Command):
    def __init__(self, commands):
        self.commands = commands
        
    def execute(self):
        help_text = "Dostupné příkazy:\n"
        for cmd, desc in self.commands.items():
            help_text += f"{cmd}: {desc}\n"
        return help_text.strip()

class ExitCommand(Command):
    def execute(self):
        return "Goodbye!"

class ShutdownCommand(Command):
    def execute(self):
        return "Server se vypíná..."

class UnknownCommand(Command):
    def execute(self):
        return "Neznámý příkaz. Pro nápovědu použijte 'help'"

# Command handler
class CommandHandler:
    def __init__(self):
        self.commands = {
            'quote': "Vrátí náhodný citát",
            'date': "Vrátí aktuální datum a čas",
            'help': "Zobrazí tuto nápovědu",
            'exit': "Ukončí spojení s klientem",
            'shutdown-server': "Vypne server"
        }
        
        self._init_commands()

    def _init_commands(self):
        self._command_objects = {
            'quote': QuoteCommand(),
            'date': DateCommand(),
            'help': HelpCommand(self.commands),
            'exit': ExitCommand(),
            'shutdown-server': ShutdownCommand()
        }

    def get_command(self, command_str: str) -> Command:
        return self._command_objects.get(command_str, UnknownCommand())

# Server implementation
class TCPServer:
    def __init__(self, host='127.0.0.1', port=65532):
        self.host = host
        self.port = port
        self.running = False
        self.handler = CommandHandler()

    def start(self):
        self.running = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host, self.port))
            s.listen(1)
            print(f"Server naslouchá na {self.host}:{self.port}")

            while self.running:
                conn, addr = s.accept()
                with conn:
                    print(f"Připojen klient: {addr}")
                    self.handle_client(conn)

    def handle_client(self, conn):
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break

            print(f"Příjem příkazu: {data}")

            command = self.handler.get_command(data)
            response = command.execute()

            conn.sendall((response + "\n").encode())

            if isinstance(command, ExitCommand):
                break
            if isinstance(command, ShutdownCommand):
                self.running = False
                break

if __name__ == "__main__":
    server = TCPServer()
    try:
        server.start()
    except KeyboardInterrupt:
        print("\nServer ukončen uživatelem")
