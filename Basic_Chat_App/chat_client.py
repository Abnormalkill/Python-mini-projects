import socket
import threading
import sys
import time

HOST = '127.0.0.1' 
PORT = 55555
ENCODING = 'utf-8'

stop_flag = threading.Event()

def receive(client_socket):
    while not stop_flag.is_set():
        try:
            message = client_socket.recv(1024).decode(ENCODING)
            
            if message == 'username?':
                pass 
            elif message:
                sys.stdout.write('\r' + ' ' * 80 + '\r')
                print(message)
                sys.stdout.write(f"You: ")
                sys.stdout.flush()
            
        except ConnectionResetError:
            print("\n[DISCONNECTED] Server connection lost.")
            stop_flag.set()
            client_socket.close()
            break
        except Exception:
            break

def write(client_socket, username):
    while not stop_flag.is_set():
        try:
            message = input("You: ")
            
            if message.lower() in ['exit', 'quit', 'stop']:
                client_socket.send('left the chat'.encode(ENCODING))
                stop_flag.set()
                break
            client_socket.send(message.encode(ENCODING))
        
        except EOFError:
            print("\n[DISCONNECTED] Exiting chat.")
            stop_flag.set()
            break
        except Exception:
            stop_flag.set()
            break
            
    client_socket.close()

def start_client():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    username = input("Enter your desired username: ")
    
    try:
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Connecting to {HOST}:{PORT}...")
        
        client.send(username.encode(ENCODING))
        
        receive_thread = threading.Thread(target=receive, args=(client,))
        receive_thread.start()
        write(client, username)

    except ConnectionRefusedError:
        print(f"[ERROR] Could not connect to the server at {HOST}:{PORT}. Ensure the server script (chat_server.py) is running.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    start_client()
