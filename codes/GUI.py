import json
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer

mixer.init()


class MainWindow:
    def __init__(self, subject):
        self.subject = subject
        self.shortcut_keys = []
        self.inserted_keys = []
        self.sound_dict = {}
        self.user_selects_a_file = 0

        self.initialize_root()
        self.load_saved_sounds()
        self.initialize_scrollbar()
        self.initialize_file_manager()
        self.initialize_shortcut_label()
        self.initialize_checkbox()

    def initialize_checkbox(self):
        self.activate_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.root, text="Activate", variable=self.activate_var).grid(column=1, row=5)

    def initialize_scrollbar(self):
        self.scroll_title = tk.Label(self.root, text="List of shortcuts:")
        self.scroll_title.grid(column=1, row=3)

        self.sb = tk.Scrollbar(self.root)
        self.mylist = tk.Listbox(self.root, width=100, yscrollcommand=self.sb.set)
        self.mylist.grid(column=1, row=4, padx=20)
        for key in self.sound_dict:
            self.__add_shortcut_to_scroll_list(key, self.sound_dict[key].split('/')[-1])

    def load_saved_sounds(self):
        try:
            with open('data.txt') as json_file:
                self.sound_dict = json.load(json_file)
        except IOError:
            pass

    def initialize_shortcut_label(self):
        self.labelStringVar = tk.StringVar()
        self.labelStringVar.set("Shortcut:   ")
        self.shortcut_label = tk.Label(self.root, textvariable=self.labelStringVar,
                                       fg="light green",
                                       bg="dark green",
                                       font="Helvetica 16 bold italic"
                                       )

    def initialize_file_manager(self):
        self.label_frame = ttk.LabelFrame(self.root, text="Open a sound file!")
        self.label_frame.grid(column=1, row=1, pady=20)
        self.initialize_button()

    def initialize_button(self):
        self.file_button = ttk.Button(self.label_frame, text="Browse A File", command=self.file_dialog)
        self.file_button.grid(column=1, row=1)

    def file_dialog(self):
        self.file_dir = filedialog.askopenfilename(initialdir="", title="Select A File", filetype=
        (("mp3 files", "*.mp3"), ("all files", "*.*")))

        if self.file_dir != '':  # if a file is selected
            self.shortcut_label.grid(column=1, row=2)
            self.user_selects_a_file = 1

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

    def __add_shortcut_to_dict(self, shortcut):
        self.sound_dict[shortcut] = self.file_dir

    def __add_shortcut_to_scroll_list(self, shortcut, file):
        list_element = shortcut + ": " + file
        self.mylist.insert(tk.END, list_element)

    def __save_dict(self):
        with open('data.txt', 'w') as outfile:
            json.dump(self.sound_dict, outfile)

    def __add_or_remove_shortcut(self, last_key):
        if last_key == 'enter':  # if user press enter key
            if len(self.shortcut_keys) == 2:  # and already pressed 2 keys before,save shortcut else do nothing
                shortcut = self.shortcut_keys[0] + self.shortcut_keys[1]
                self.__add_shortcut_to_dict(shortcut)
                self.__add_shortcut_to_scroll_list(shortcut, self.file_dir.split('/')[-1])
                self.__save_dict()

                self.shortcut_keys.clear()
                self.shortcut_label.grid_forget()
                self.user_selects_a_file = 0

        elif last_key == 'backspace':  # if user press backspace key
            if len(
                    self.shortcut_keys) != 0:  # and already pressed 1 or 2 keys before, delete one of them else do nothing
                self.shortcut_keys.pop()

        elif len(self.shortcut_keys) < 2:  # add only 2 keys in shortcut
            self.shortcut_keys.append(last_key)

    def __find_shortcut(self):
        shortcut = self.inserted_keys[-2] + self.inserted_keys[-1]
        if self.sound_dict.__contains__(shortcut):
            return self.sound_dict[shortcut]
        else:
            return None

    def __play_sound_if_exists(self):
        sound_dir = self.__find_shortcut()
        if sound_dir is not None:
            mixer.music.load(sound_dir)
            mixer.music.play()
            return True
        return False

    def __add_inserted_shortcut(self, last_key):
        self.inserted_keys.append(last_key)
        if len(self.inserted_keys) >= 2:
            played = self.__play_sound_if_exists()
            if played:
                self.inserted_keys.clear()  # make list empty

    def update(self):
        last_key = self.subject.get_last_key()  # get last key pressed by user
        if last_key == 'f2':  # deactivate listening
            self.activate_var.set(0)
        elif last_key == 'f3': # activate listening
            self.activate_var.set(1)
        else:
            if self.user_selects_a_file:
                self.__add_or_remove_shortcut(last_key)
                current = self.__prepare_print_shortcut()

                self.labelStringVar.set("Shortcut:   " + current)
                self.root.update_idletasks()
            else:
                if last_key == 'esc':  # if user press escape button ---> it stops playing sound
                    mixer.music.stop()
                elif self.activate_var.get() == 1:  # if listening is active
                    self.__add_inserted_shortcut(last_key)
