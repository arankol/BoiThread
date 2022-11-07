import json
import os
import sys
from socket import *
import threading
HOST = 'localhost'  # внутренний служебный адрес текущей машины
PORT = 65485        # любой свободный порт
addr = (HOST,PORT)
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(addr)
users = []

def xod(n,m):
    while users[m]['broken'] != 2 and users[n]['broken'] != 2:
        if users[n]['msg']:
            coordx, coordy = users[n]['msg'].pop(0)
            if users[m]['map'][coordx][coordy] == 0 or users[m]['map'][coordx][coordy] == '●' or users[m]['map'][coordx][coordy] == '▪':
                udp_socket.sendto('0'.encode(), users[n]['addr'])
                users[m]['map'][coordx][coordy] = '▪'
            else:
                users[m]['broken'] += 1
                users[m]['map'][coordx][coordy] = '●'
                udp_socket.sendto('1'.encode(), users[n]['addr'])
            if users[m]['broken'] == 2:
                udp_socket.sendto('Проиграл'.encode(), users[m]['addr'])
                udp_socket.sendto('Победа'.encode(), users[n]['addr'])
                exit()
            udp_socket.sendto('Стреляй'.encode(), users[n]['addr'])

t1 = threading.Thread(target=xod, args=(0, 1), daemon=False)
t2 = threading.Thread(target=xod, args=(1, 0), daemon=False)
start = 0

while True:
    while len(users) < 2:
        data, addr = udp_socket.recvfrom(1024)
        a = json.loads(data)
        user = {
            'addr':addr,
            'map': a,
            'broken': 0,
            'msg': []
        }
        if users:
            if users[0]['addr'] != addr:
                users.append(user)
        else:
            users.append(user)
        if start != 2:
            start += 1
        if start == 2:
            udp_socket.sendto('Стреляй'.encode(), users[0]['addr'])
            udp_socket.sendto('Стреляй'.encode(), users[1]['addr'])
            t1.start()
            t2.start()
    if users[0]['broken'] == 2 or users[1]['broken'] == 2:
        break
    data, addr = udp_socket.recvfrom(1024)
    coord = json.loads(data)
    coordx, coordy = coord
    if users[0]['addr'] == addr:
        users[0]['msg'].append((coordx, coordy))
    else:
        users[1]['msg'].append((coordx, coordy))









    #udp_socket.sendto(data, addr)

udp_socket.close()

