# Функція шифрування данних, чку раніше робили
def encrypt(text,s):
    result = ""
    # Формування шифрованого тексту
    for i in range(len(text)):
      char = text[i]
      #Умова вибору алгоритму шифрування для симолів латиниці по коду в таблиці Unicode. 65 код великої латинської ліери А, а 122 - маленької z
      if(ord(char)>=65 and ord(char)<=122):
          # Шифрування символів верхнього регістру. 26 - кількість букв в алфовіті латиниці
          if (char.isupper()):
             result += chr((ord(char) + s-65) % 26 + 65)
          # Шифорування симвлів нижнього регістру. 97 - код маленької букви а
          else:
             result += chr((ord(char) + s - 97) % 26 + 97)
      #Умова вибору алгоритму шифрування для симолів кирилиці по коду в таблиці Unicode. 
      #1040 код великої латинської ліери А, а 1071 - великої літери Я,
      #1072 - маленька літера а, 1104 - маленька літера я. 32 - кількість символів.
      if(ord(char)>=1040 and ord(char)<=1071):
          # Шифрування символів верхнього регістру.
             result += chr((ord(char) + s - 1040) % 32 + 1040)
          # Шифорування симвлів нижнього регістру
      if(ord(char)>=1072 and ord(char)<1104):
             result += chr((ord(char) + s - 1072) % 32 + 1072)
      #Умова шифрування символів, які не належать ні до латиниці ні до кирилиці. Залишаємо їх без змін.
      if(not (ord(char)>=65 and ord(char)<=122) and not (ord(char)>=1040 and ord(char)<=1105)):
          result +=char
    return result

# Для роботи з сокетами підключаємо модуль socket
import socket 
# Нам треба отримувати і відправляти повідомлення одночасно.
# Або не залежно один від одного. Для цього нам буде потрібно багатопоточне виконання нашого коду.
# Тому ми будемо використовувати модуль threading
import threading
def read_sok(): # Функція, яка буде отримувати повідомлення від сервера
     while 1 :
         data = sor.recv(1024) # Буфер в байтах
         print(data.decode('utf-8'))
server = '192.168.0.73', 8080  # Дані сервера
alias = input("Введіть Ваше ім'я чи нік: ") # Вводимо наш псевдонім

# socket.AF_INET — для сокета використовуємо протокол IPv4. 
# socket.SOCK_DGRAM — тип сокета. Датаграммный сокет це сокет, призначений для передачі даних у вигляді 
# окремих повідомлень (датаграмм). У порівнянні з потоковим сокетом, обмін даними відбувається швидше. 
# Датаграммним сокет допускає передачу повідомлення кільком одержувачам (multicasting) 
# і трансляційну передачу (broadcasting).
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sor.bind(('', 0)) # Задаємо сокет як клієнт


sor.sendto((alias+' підключився до Сервера').encode('utf-8'), server)# Повідомлємо сервер про підключення

# Створюємо поток і запускаємо на ньому функцію read_sok
potok = threading.Thread(target= read_sok)
potok.start()
while 1 : # Зациклюємо отримання і відправку повідомлень.
     mensahe = encrypt(input("> "),4) # Отримуємо дані і шифруємо шифром Цезаря з ключем 4 для відправки
     sor.sendto(('['+alias+']'+": "+mensahe).encode('utf-8'), server)