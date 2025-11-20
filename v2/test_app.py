# test_app.py
import tkinter as tk
from tkinter import ttk
import random

class TestApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test App - Coba Edit Warna!")
        self.root.geometry("500x400")
        self.setup_ui()
    
    def setup_ui(self):
        # COBA EDIT BAGIAN INI DAN LIHAT PERUBAHAN!
        
        # Title - coba ganti text atau warna
        title = tk.Label(
            self.root, 
            text="🎉 Tkinter Live Reload Demo!",  # <-- EDIT INI
            font=("Arial", 18, "bold"),
            fg="blue",  # <-- COBA GANTI JADI "red", "green", dll
            bg="lightyellow"
        )
        title.pack(pady=20)
        
        # Button dengan style berbeda
        self.button = ttk.Button(
            self.root, 
            text="Click untuk Demo!",  # <-- EDIT TEXT INI
            command=self.on_button_click
        )
        self.button.pack(pady=10)
        
        # Result label
        self.result = tk.Label(
            self.root, 
            text="Status: Aplikasi jalan!",
            font=("Arial", 12),
            fg="darkgreen"
        )
        self.result.pack(pady=10)
        
        # Progress bar dengan random value
        self.progress = ttk.Progressbar(self.root, length=300, mode='determinate')
        self.progress.pack(pady=10)
        self.progress['value'] = 30  # <-- COBA GANTI ANGKA INI
        
        # Text area
        self.text_area = tk.Text(self.root, height=5, width=50)
        self.text_area.pack(pady=10)
        self.text_area.insert('1.0', "Edit kode dan lihat perubahan realtime!\nCoba ganti teks ini di source code...")
    
    def on_button_click(self):
        colors = ["red", "green", "blue", "purple", "orange"]
        new_color = random.choice(colors)
        self.result.config(text=f"Color changed to: {new_color}", fg=new_color)
        self.progress['value'] = random.randint(0, 100)
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = TestApp()
    app.run()