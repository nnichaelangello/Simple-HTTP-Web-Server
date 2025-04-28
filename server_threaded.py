import socket
import sys
import threading

# Membuat server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengikat server ke alamat dan port
serverSocket.bind(('127.0.0.1', 6789))
serverSocket.listen(5)  # Maksimum 5 koneksi dalam antrian

print('Server siap menerima permintaan...')

def handle_client(connectionSocket, addr):
    try:
        # Menerima pesan dari klien
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.read()
        f.close()

        # Mengirim header HTTP
        connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())
        
        # Mengirim konten file
        connectionSocket.send(outputdata.encode())
        connectionSocket.send('\r\n'.encode())
    except IOError:
        # Mengirim respons 404 jika file tidak ditemukan
        connectionSocket.send('HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
    finally:
        # Menutup koneksi klien
        connectionSocket.close()

while True:
    try:
        # Menerima koneksi klien
        connectionSocket, addr = serverSocket.accept()
        print(f'Koneksi dari {addr}')
        
        # Membuat thread baru untuk menangani klien
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
        client_thread.start()
    except KeyboardInterrupt:
        print("\nServer dimatikan.")
        serverSocket.close()
        sys.exit()