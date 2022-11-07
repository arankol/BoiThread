import json
from socket import *

HOST = 'localhost'  # ip-адрес сервера, мы знаем, что он будет запущен на той же машине, что и клиент
PORT = 65485        # мы знаем, что сервер слушает порт 65432
addr = (HOST, PORT)
upd_socket = socket(AF_INET, SOCK_DGRAM)

Nameup = [' ','1','2','3','4','5','6','7','8','9','10']
Namebot = ['A','B','C','D','E','F','G','H','I','J']
A = [[0] * 10 for _ in range(10)]

def regular():
    global g,h
    g = input('\nВведите строку ')
    if g == 'a' or g == 'A':
        g = 1
    elif g == 'b' or g == 'B':
        g = 2
    elif g == 'c' or g == 'C':
        g = 3
    elif g == 'd' or g == 'D':
        g = 4
    elif g == 'e' or g == 'E':
        g = 5
    elif g == 'f' or g == 'F':
        g = 6
    elif g == 'g' or g == 'G':
        g = 7
    elif g == 'h' or g == 'H':
        g = 8
    elif g == 'i' or g == 'I':
        g = 9
    elif g == 'j' or g == 'J':
        g = 10
    h = int(input('\nВведите столбец '))

def Bibod(a,A):
    print('\n')
    print(a, '\n')
    print(*Nameup)
    i = 0
    for row in A:
        print(*Namebot[i], end=' ')
        print(*row)
        i += 1

def BBOD(k, o, answer):
    l = 0
    regular()
    if answer == 1:
        for i in range(o):
            A[g - 1][h + l - 1] = k
            l += 1
    if answer == 2:
        for i in range(o):
            A[g + l - 1][h - 1] = k
            l += 1
    Bibod('Твоя карта кораблей',A)
    l = 0


def Korabl(c,u):
            answer = int(input('\nВведите 1 для установки по горизонтали или 2 по вертикали = '))
            BBOD(c,u,answer)

for i in range(4):
   print('\nВведите однопалубник, осталось = ',4-i)
   BBOD(1,1,1)
for i in range(3):
    print('\nВведите двухпалубник, осталось = ',3-i)
    Korabl(2,2)
for i in range(2):
    print('\nВведите трехпалубник, осталось = ',2-i)
    Korabl(3,3)
for i in range(1):
    print('\nВведите четврехпалубник, осталось = ',1-i)
    Korabl(4,4)

Bibod('Твоя карта',A)
j = json.dumps(A)
data = j.encode()
upd_socket.sendto(data, addr)
for i in range(10):
    for j in range(10):
        A[i][j] = '◯'
while True:
    data, addr = upd_socket.recvfrom(1024)
    if data.decode() == 'Проиграл':
        print('Ты проиграл')
        break
    elif data.decode() == 'Победа':
        print('Ты победил')
        break
    if data.decode() == '1':
        print('Попал')
        coordx, coordy = coord
        A[coordx][coordy] = '●'
        Bibod('Карта куда ты попал',A)
    elif data.decode() == '0':
        print('Попал')
        coordx, coordy = coord
        A[coordx][coordy] = '▪'
        Bibod('Карта куда ты попал',A)
    if data.decode() == 'Стреляй':
        print('Стреляй')
        regular()
        coord = [g - 1, h - 1]
        data = json.dumps(coord)
        data = data.encode()
        upd_socket.sendto(data, addr)







         
      
     



