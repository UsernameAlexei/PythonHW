import socket
import time
from Data_collection_class import Collection
from datetime import datetime
from contextlib import closing

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 9999))
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
        metric_name = 'press the key in 1 min'
        result = [time_now, metric_name, keystrokes.get_current_state()]
        s.send(str(result).encode('utf-8'))
        resp = s.recv(1024)
        print(resp.decode('utf-8'))


