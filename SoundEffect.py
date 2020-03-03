import threading
import codes.GUI as GUI
import codes.KeyLogger as Logger
import codes.Subject as Subject


# this class run a thread activate key logger :
class LoggerThread(threading.Thread):
    def __init__(self, subject):
        super().__init__()
        self.subject = subject

    def run(self):
        logger = Logger.Keylogger(self.subject)
        logger.start()


def main():
    subject = Subject.SubjectClass()

    logger_thread = LoggerThread(subject)
    logger_thread.start()

    main_window = GUI.MainWindow(subject)
    subject.set_observer(main_window)
    main_window.start()


if __name__ == '__main__':
    main()
