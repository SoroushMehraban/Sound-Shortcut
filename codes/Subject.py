class SubjectClass:
    def __init__(self):
        self.observer = None
        self.__buffer = ''
        self.__key = ''

    def get_buffer(self):
        return self.__buffer

    def get_last_key(self):
        return self.__key

    def set_buffer_key(self, buffer, key):
        self.__buffer = buffer
        self.__key = key
        self.notify_observer()

    def set_observer(self, observer):
        self.observer = observer

    def notify_observer(self):
        self.observer.update()
