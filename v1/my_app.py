# my_app.py
import tkinter as tk
from tkinter import ttk
import time

class SampleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My App - Edit dan lihat perubahan!")
        self.root.geometry("400x300")
        self.setup_ui()
        
        # Tambahkan timestamp untuk lihat reload bekerja
        self.timestamp_label = ttk.Label(self.root, text=f"Started: {time.strftime('%H:%M:%S')}")
        self.timestamp_label.pack(pady=10)
    
    def setup_ui(self):
        # UI components - edit ini dan lihat perubahan!
        title = ttk.Label(self.root, text="Hello Tkinter!", font=("Arial", 16))
        title.pack(pady=20)
        
        self.entry = ttk.Entry(self.root, width=30)
        self.entry.pack(pady=10)
        self.entry.insert(0, "Coba edit teks ini di kode...")
        
        button = ttk.Button(self.root, text="Click Me!", command=self.on_click)
        button.pack(pady=10)
        
        self.result_label = ttk.Label(self.root, text="Status: Ready")
        self.result_label.pack(pady=10)
        
        # Progress bar untuk demo
        self.progress = ttk.Progressbar(self.root, length=200, mode='determinate')
        self.progress.pack(pady=10)
        self.progress['value'] = 50
        
        # ComboBox example
        self.combo = ttk.Combobox(self.root, values=["Option 1", "Option 2", "Option 3"])
        self.combo.pack(pady=10)
        self.combo.set("Option 1")
    
    def on_click(self):
        self.result_label.config(text=f"Clicked! Entry: {self.entry.get()}")
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = SampleApp()
    app.run()