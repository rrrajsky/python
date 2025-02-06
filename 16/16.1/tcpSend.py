import socket

def start_server():
    # Vytvoření socketu
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Nastavení adresy a portu
    server_address = ('127.0.0.1', 65532)
    
    # Připojení socketu k adrese a portu
    server_socket.bind(server_address)
    
    # Naslouchání připojení (maximálně 1 připojení ve frontě)
    server_socket.listen(1)
    
    print(f"Server naslouchá na {server_address}")
    
    while True:
        # Čekání na připojení klienta
        print("Čekání na připojení...")
        client_socket, client_address = server_socket.accept()
        
        try:
            print(f"Připojení od {client_address}")
            
            # Odeslání zprávy "HELLO" klientovi
            message = "HELLO"
            client_socket.sendall(message.encode('utf-8'))
            
        finally:
            # Uzavření spojení s klientem
            client_socket.close()
            print(f"Spojení s {client_address} ukončeno")

if __name__ == "__main__":
    start_server()
