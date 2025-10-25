import socket
import threading

HOST = '127.0.0.1'
PORT = 55555
ENCODING = 'utf-8'

clients = []
usernames = []

def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                username = usernames[index]
                usernames.remove(username)
                print(f"[DISCONNECTED] {username}")
                broadcast(f'[SERVER] {username} left the chat.'.encode(ENCODING), client)


def handle_client(client):
    
    try:
        username = client.recv(1024).decode(ENCODING)
        usernames.append(username)
        clients.append(client)
        
        print(f"[NEW CONNECTION] {username} connected from {str(client.getpeername())}")

        broadcast(f'[SERVER] {username} joined the chat!'.encode(ENCODING), client)
        client.send('Connected to the server. Start chatting!'.encode(ENCODING))

        while True:
            try:
                message = client.recv(1024)
                if not message:
                    break
                
                full_message = f'{username}: {message.decode(ENCODING)}'
                print(f"[MESSAGE] {full_message}")
                broadcast(full_message.encode(ENCODING), client)
                
            except:
                break

    finally:
        if client in clients:
            index = clients.index(client)
            clients.remove(client)
            username = usernames[index]
            usernames.remove(username)
            client.close()
            print(f"[DISCONNECTED] {username}")
            broadcast(f'[SERVER] {username} left the chat.'.encode(ENCODING), None)


def start_server():
    """Initializes and runs the server."""
    print("[STARTING] Server is starting...")
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        client, address = server.accept()
        
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") 

if __name__ == "__main__":
    start_server()
