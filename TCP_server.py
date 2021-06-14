import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((('localhost', 9999)))
sock.listen(3)

while True:
    client, addr = sock.accept()
    print('Connected: ', addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        udata = data.decode()
        client.send(udata.encode('utf-8'))
        # save to file
        with open('keystrokes.txt', 'a') as f:
            f.write(udata + '\n')

    client.close()
