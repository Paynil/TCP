import re
import math
import socket

HOST = "challenge01.root-me.org"
PORT = 52002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Cоединение с HOST и PORT
    data = s.recv(1024)
    numbers = re.findall(r'\d+', data.decode())

    A = int(numbers[0]) if len(numbers[0]) == 3 else int(numbers[1])
    B = int(numbers[-1]) if len(numbers[-1]) == 4 else int(numbers[0])

    print("Число (A):", A)
    print("Число (B):", B)

    result = (A ** 0.5) * B
    result = round(result, 2)
    c=bytes(str(result)+"\n",'utf-8')  # Преобразовать результат в байты с добавлением новой строки
    s.send(c)
    data2=s.recv(1024)

print(f"Received {data2!r}")