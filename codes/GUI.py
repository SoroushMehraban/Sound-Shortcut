import tkinter as tk
from tkinter import ttk, filedialog


class MainWindow:
    def __init__(self, subject):
        self.subject = subject
        self.shortcut_keys = []

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
        print(file_name)

    def initialize_root(self):
        self.root = tk.Tk()
        self.root.title("Sound effect")
        self.root.minsize(640, 400)

    def start(self):
        self.root.mainloop()

    def update(self):
        last_key = self.subject.get_last_key()

        if last_key == 'enter':
            self.shortcut_keys = []
        elif last_key == 'backspace':
            self.shortcut_keys.pop()
        else:
            self.shortcut_keys.append(last_key)

        if len(self.shortcut_keys) != 0:
            current = self.shortcut_keys[0]
            for key in self.shortcut_keys[1:]:
                current += '+' + key
        else:
            current = ''

        self.labelStringVar.set("Shortcut:   " + current)
        self.root.update_idletasks()
