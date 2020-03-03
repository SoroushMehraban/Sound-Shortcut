class SubjectClass:
    def __init__(self):
        self.observer = None
        self.__buffer = ''

    def get_buffer(self):
        return self.__buffer

    def set_buffer(self, buffer):
        self.__buffer = buffer
        self.notify_observer()

    def set_observer(self, observer):
        self.observer = observer

    def notify_observer(self):
        self.observer.update()
