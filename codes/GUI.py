import tkinter as tk


class MainWindow:
    def __init__(self, subject):
        self.root = tk.Tk()

        self.subject = subject

        self.label = None
        self.labelStringVar = tk.StringVar()

    def start(self):
        self.labelStringVar.set("Hi!")
        self.label = tk.Label(self.root, textvariable=self.labelStringVar)
        self.label.pack()
        self.root.mainloop()

    def update(self):
        self.labelStringVar.set(self.subject.get_buffer())
        self.root.update_idletasks()
