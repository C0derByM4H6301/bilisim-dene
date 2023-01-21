import socket
import sys

HOST = ''   # IP adresi
PORT = 8888 # Port numarası

# Socket oluştur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket oluşturuldu')

# Bağlantı noktasını tanımla
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bağlantı noktası tanımlanamadı. Hata: ' + str(msg[0]) + ': ' + msg[1])
    sys.exit()

print('Bağlantı noktası tanımlandı')

# Bağlantıları dinle
s.listen(10)
print('Bağlantılar dinleniyor...')

# Bağlantı kabul et
conn, addr = s.accept()

# Bağlantı adresini ekrana yazdır
print('Bağlantı kabul edildi. Bağlantı adresi: ' + addr[0] + ':' + str(addr[1]))

# Gelen veriyi log.txt dosyasına kaydet
with open("log.txt", "a") as log:
    log.write("Gelen veri: " + addr[0] + ": " + data.decode() + "\n")

# Bağlantıyı kapat
conn.close()
