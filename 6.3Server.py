#SERVER CODE
import socket
import math
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
   while True:
      s_sock.send(str.encode('Welcome to the Server\n'))
      while True:
        input = s_sock.recv(2048)
        input = input.decode('utf-8')
        print(input)

        if not input:
           break


        message = "Enter number: "

#while True:
        if input == '1':
           data = s_sock.recv(2048)
           data = int(data)
           calc = str(math.log(data))
           print(type(calc))

        elif input == '2':
           data = s_sock.recv(2048)
           data = int (data)
           calc = str(math.sqrt(data))
           print(calc)

        elif input == '3':
           data = s_sock.recv(2048)
           data = int(data)
           calc = str(math.exp(data))
           print(calc)

        else:
           calc = "Wrong input"

        s_sock.sendall(str.encode(calc))
      s_sock.close()

if __name__ == '__main__':
   s = socket.socket()
   s.bind(('',8881))
   print("*** listening ***")
   s.listen(5)
   try:
      while True:
        try:
           s_sock, s_addr = s.accept()
           p = Process(target=process_start, args=(s_sock,))
           p.start()
           print(f"[+] Connecting to {s_addr}")

        except socket.error:
           print('got a socket error')

   except Exception as e:
      print('an exception occurred!')
      print(e)
      sys.exit(1)
   finally:
      s.close()

