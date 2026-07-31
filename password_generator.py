import os
os.system('cls' if os.name == 'nt' else 'clear')
import tkinter as tk
import random
import string as str
def generate_password():
    symbols = str.ascii_letters + str.digits
    password ="".join(random.choice(symbols)for _ in range(12))
    entry.delete(0,tk.END)
    entry.insert(0, password)   
def copy_password():
    password = entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#1E1E1E")

label = tk.Label(
    root, 
    text="Hello! This is a Password Generator.", 
    font=("Segoe UI", 12), 
    bg="#1E1E1E",  
    fg="#FFFFFF"   
)
label.pack(pady=10)
entry = tk.Entry(
    root,
    font=("Consolas", 16),
    bg="#2D2D2D",               
    fg="#00FF66",               
    insertbackground="white",   
    justify="center",           
    relief="flat"               
)   
entry.pack(pady=10)
button = tk.Button(
    root,
    text ="Generate", 
    font=("Segoe UI", 12, "bold"),
    bg="#007ACC",               
    fg="white",                 
    activebackground="#005999", 
    activeforeground="white",
    relief="flat",              
    cursor="hand2",
    command = generate_password
)
button.place(x=60, y=100)
second_button = tk.Button(
    root,
    text ="Copy password",
    font=("Segoe UI", 12),
    bg="#3C3C3C",
    fg="white",
    activebackground="#505050",
    activeforeground="white",
    relief="flat",
    cursor="hand2", 
    command=copy_password
)
second_button.place(x=180, y=100)

root.mainloop()