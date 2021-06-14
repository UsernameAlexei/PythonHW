import threading
import keyboard
import pyautogui


# counting keystrokes
class Collection(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, target=self.start_collect)
        self.counter = 0
        self.running = False

    def start_collect(self):
        self.running = True
        not_pressed = True

        while self.running:
            keyboard.read_key()
            if not_pressed:
                self.counter += 1
                print(self.counter)
                not_pressed = False
            else:
                not_pressed = True

    def get_current_state(self):
        return self.counter

    def cleanup(self):
        self.counter = 0

    def stop_collect(self):
        self.running = False
        pyautogui.press('esc')
        self.counter -= 1
        threading.Thread.join(self)

# a = Collection()
# a.start()
# time.sleep(5)
# a.stop_collect()
