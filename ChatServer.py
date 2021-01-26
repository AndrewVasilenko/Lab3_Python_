# Для роботи з сокетами підключаємо модуль socket
import socket

# socket.AF_INET — для сокета використовуємо протокол IPv4. 
# socket.SOCK_DGRAM — тип сокета. Датаграммный сокет це сокет, призначений для передачі даних у вигляді 
# окремих повідомлень (датаграмм). У порівнянні з потоковим сокетом, обмін даними відбувається швидше. 
# Датаграммним сокет допускає передачу повідомлення кільком одержувачам (multicasting) 
# і трансляційну передачу (broadcasting).
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('',8080)) # звяжемо сокет з адресом(інтерфейсом) і портом :
client = [] # Масив где зберігаємо адреси клиентів
print ('Start Server')
while 1 :
         # Нам необхідно отримувати і відправляти дані іншим відомим клієнтам. 
         # Для цього, ми будемо використовувати функцію socket.recvfrom (bufsize) 
         # яка нам поверне дані та адресу сокета з якого отримані ці дані.
         data , addres = sock.recvfrom(1024)
         print (addres[0], addres[1])
         if  addres not in client : 
                 client.append(addres)# Якщо такого клиєнта немає, то добавляємо
         for clients in client :
                 if clients == addres : 
                     continue # Не відправлять дані кліенту, який їх прислав
                 sock.sendto(data,clients) # Для відправки даних будемо використовувати функцію socket.sendto (bytes, address)