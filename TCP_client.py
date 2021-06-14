import socket
import time
from Data_collection_class import Collection
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))

while True:
    # launch counting keystrokes per minute
    keystrokes = Collection()
    keystrokes.cleanup()
    keystrokes.start()
    time.sleep(60)
    keystrokes.stop_collect()
    # time tracking
    time_now = datetime.now()
    time_now = time_now.strftime("%H:%M:%f")

    result = [time_now, f'{keystrokes.get_current_state()} press the key in 1 min']

    sock.send(str(result).encode('utf-8'))
    resp = sock.recv(1024)
    print(resp.decode('utf-8'))

# sock.close()

