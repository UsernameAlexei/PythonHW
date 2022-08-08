import time
import pyautogui
import unittest
from Data_collection_class import Collection


class Test_collection_class(unittest.TestCase):
    def test_start_collection(self):
        test = Collection()
        test.start()
        pyautogui.press('ctrl', presses=10)
        time.sleep(5)
        test.stop_collect()
        self.assertEqual(10, test.get_current_state())

    def test_cleanup(self):
        test = Collection()
        test.start()
        pyautogui.press('ctrl', presses=10)
        time.sleep(5)
        test.stop_collect()
        test.cleanup()
        self.assertEqual(0, test.get_current_state())
