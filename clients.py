import socket

HOST = '127.0.0.1'  # Hedef sunucunun IP adresi
PORT = 8888        # Hedef sunucunun port numarası
MESSAGE = "Merhaba Dünya" # Atılacak string

# Socket oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucuya bağlan
s.connect((HOST, PORT))

# Veriyi gönder
s.sendall(MESSAGE.encode())

# Bağlantıyı kapat
s.close()
