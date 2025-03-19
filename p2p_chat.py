import socket
import threading
import os
import sys
import ssl
import socks
from bleak import BleakClient, BleakScanner  # Modern Bluetooth library
import json
from cryptography.fernet import Fernet

# Load or generate an encryption key
KEY_FILE = "encryption_key.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

cipher = Fernet(key)

# Configure Tor Proxy
def setup_tor():
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

# Function to send messages securely
def send_message(conn, mode):
    while True:
        msg = input("Send: ")
        encrypted_msg = cipher.encrypt(msg.encode())
        conn.send(encrypted_msg)

        if msg.lower() == "exit":
            conn.close()
            break

# Function to receive messages securely
def receive_message(conn):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            decrypted_msg = cipher.decrypt(data).decode()
            print(f"\n[Received] {decrypted_msg}")
        except:
            print("\n🔴 Connection lost.")
            break

# Function to send files securely
def send_file(conn):
    file_path = input("Enter file path: ")
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return

    with open(file_path, "rb") as f:
        encrypted_data = cipher.encrypt(f.read())

    file_name = os.path.basename(file_path)
    conn.send(json.dumps({"filename": file_name}).encode())
    conn.send(encrypted_data)
    print("✅ File sent successfully.")

# Function to receive files securely
def receive_file(conn):
    metadata = json.loads(conn.recv(1024).decode())
    file_name = metadata["filename"]
    encrypted_data = conn.recv(1000000)  # Large buffer for file transfer

    decrypted_data = cipher.decrypt(encrypted_data)
    with open(f"received_{file_name}", "wb") as f:
        f.write(decrypted_data)
    print(f"✅ File received: received_{file_name}")

# Function to run the server
def start_server(mode):
    if mode == "tor":
        setup_tor()
        host = "127.0.0.1"
    else:
        host = socket.gethostbyname(socket.gethostname())

    port = 65432
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"🟢 Server started on {host}:{port}, waiting for connection...")

    conn, addr = server.accept()
    print(f"🔗 Connected to {addr}")

    threading.Thread(target=receive_message, args=(conn,)).start()
    while True:
        choice = input("Type 'msg' to send message, 'file' to send file, 'exit' to quit: ").lower()
        if choice == "msg":
            send_message(conn, mode)
        elif choice == "file":
            send_file(conn)
        elif choice == "exit":
            conn.close()
            break

# Function to connect as a client
def start_client(mode):
    if mode == "tor":
        setup_tor()
        host = "127.0.0.1"
    else:
        host = input("Enter server IP: ")

    port = 65432
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"🔗 Connected to server {host}:{port}")

    threading.Thread(target=receive_message, args=(client,)).start()
    while True:
        choice = input("Type 'msg' to send message, 'file' to send file, 'exit' to quit: ").lower()
        if choice == "msg":
            send_message(client, mode)
        elif choice == "file":
            send_file(client)
        elif choice == "exit":
            client.close()
            break

# Function for Bluetooth Offline Mode
def start_bluetooth():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)

    port = server_socket.getsockname()[1]
    print(f"🔵 Waiting for a Bluetooth connection on port {port}...")

    client_socket, client_info = server_socket.accept()
    print(f"🔗 Bluetooth connected to {client_info}")

    while True:
        msg = input("Send: ")
        client_socket.send(msg.encode())
        if msg.lower() == "exit":
            break
    client_socket.close()
    server_socket.close()

# Main function to select mode
def main():
    print("🔹 Select Communication Mode:")
    print("1️⃣ Tor (Anonymous Internet)")
    print("2️⃣ LAN (Local Network, No Internet)")
    print("3️⃣ Bluetooth (Offline Short-Range)")

    mode_choice = input("Enter choice (1/2/3): ")
    if mode_choice == "1":
        mode = "tor"
    elif mode_choice == "2":
        mode = "lan"
    elif mode_choice == "3":
        start_bluetooth()
        return
    else:
        print("❌ Invalid choice.")
        return

    role = input("Start as (server/client): ").lower()
    if role == "server":
        start_server(mode)
    elif role == "client":
        start_client(mode)
    else:
        print("❌ Invalid role.")

if __name__ == "__main__":
    main()