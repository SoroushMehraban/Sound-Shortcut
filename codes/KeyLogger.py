import time
from pynput.keyboard import Listener
import threading

input_buffer = ''  # a buffer to store inserted keys ( Resets each 5 sec )


# this class run a thread to clear input buffer each 5 sec:
class BufferThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            time.sleep(5)  # wait for 5 sec
            reset_buffer()


# this function resets buffer whenever it is called
def reset_buffer():
    global input_buffer
    input_buffer = ''


# this function is called whenever a key is pressed on keyboard ( with help of listener)
def on_press(key):
    global input_buffer

    if str(key)[
        0] is '\'':  # if a normal key is pressed like 's' ---> we save s instead of 's' (removing first and last letter)
        input_buffer += str(key)[1:-1]
    else:
        input_buffer += str(key)
    print(input_buffer)


# our main function that starts when we run our code
def start():
    buffer_thread = BufferThread()  # creating object of our thread
    buffer_thread.start()  # start our thread
    with Listener(on_press=on_press) as listener:  # listener to listen key pressing and calling on_press function
        listener.join()
