import threading
import time
import keyboard


# counting keystrokes
class Collection(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, target=self.start_collect)
        self.counter = 0
        self.running = False

    def handler(self, even):
        self.counter += 1

    def start_collect(self):
        self.running = True

        keyboard.on_press(self.handler)
        while self.running:
            # just waiting small time for saving CPU time
            time.sleep(0.01)

    def get_current_state(self):
        return self.counter

    def cleanup(self):
        self.counter = 0

    def stop_collect(self):
        self.running = False
        keyboard.unhook_all()
        threading.Thread.join(self)
