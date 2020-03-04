import tkinter as tk
from tkinter import ttk, filedialog


class MainWindow:
    def __init__(self, subject):
        self.subject = subject
        self.shortcut_keys = []
        self.file_selected_flag = 0

        self.initialize_root()
        self.initialize_file_manager()
        self.initialize_shortcut_label()

    def initialize_shortcut_label(self):
        self.labelStringVar = tk.StringVar()
        self.labelStringVar.set("Shortcut:   ")
        self.shortcut_label = tk.Label(self.root, textvariable=self.labelStringVar,
                                       fg="light green",
                                       bg="dark green",
                                       font="Helvetica 16 bold italic"
                                       )
        self.shortcut_label.grid(column=2, row=1, padx=20, pady=20)

    def initialize_file_manager(self):
        self.label_frame = ttk.LabelFrame(self.root, text="Open a sound file!")
        self.label_frame.grid(column=1, row=1, padx=20, pady=20)
        self.initialize_button()

    def initialize_button(self):
        self.file_button = ttk.Button(self.label_frame, text="Browse A File", command=self.file_dialog)
        self.file_button.grid(column=1, row=1)

    def file_dialog(self):
        file_name = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("mp3 files", "*.mp3"), ("all files", "*.*")))
        self.file_selected_flag = 1
        print(file_name)

    def initialize_root(self):
        self.root = tk.Tk()
        self.root.title("Sound effect")
        self.root.minsize(640, 400)

    def start(self):
        self.root.mainloop()

    def __prepare_print_shortcut(self):
        if len(self.shortcut_keys) != 0:
            current = self.shortcut_keys[0]
            for key in self.shortcut_keys[1:]:
                current += '+' + key
        else:
            current = ''
        return current

    def __add_or_remove_shortcut(self, last_key):
        if last_key == 'enter':  # if user press enter key
            if len(self.shortcut_keys) == 2:  # and already pressed 2 keys before,save shortcut else do nothing
                self.shortcut_keys = []
                self.file_selected_flag = 0

        elif last_key == 'backspace':  # if user press backspace key
            if len(
                    self.shortcut_keys) != 0:  # and already pressed 1 or 2 keys before, delete one of them else do nothing
                self.shortcut_keys.pop()

        elif len(self.shortcut_keys) < 2:  # add only 2 keys in shortcut
            self.shortcut_keys.append(last_key)

    def update(self):
        print(self.file_selected_flag)
        if self.file_selected_flag:
            last_key = self.subject.get_last_key()  # get last key pressed by user

            self.__add_or_remove_shortcut(last_key)
            current = self.__prepare_print_shortcut()

            self.labelStringVar.set("Shortcut:   " + current)
            self.root.update_idletasks()
