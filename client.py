import socket
import sys

# Memeriksa argumen baris perintah
if len(sys.argv) != 4:
    print("Penggunaan: python client.py server_host server_port filename")
    sys.exit(1)
    
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# Membuat socket klien
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
try:
    # Menghubungkan ke server
    clientSocket.connect((server_host, server_port))
        
    # Membuat dan mengirim permintaan HTTP GET
    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
    clientSocket.send(request.encode())
        
    # Menerima dan menampilkan respons
    response = ''
    while True:
        data = clientSocket.recv(1024).decode()
        if not data:
            break
        response += data
        
    print("Respons dari server:")
    print(response)
        
except Exception as e:
    print(f"Error: {e}")
finally:
    clientSocket.close()