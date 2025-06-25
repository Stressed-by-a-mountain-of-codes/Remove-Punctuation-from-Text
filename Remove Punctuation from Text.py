import tkinter as tk
from tkinter import messagebox
import pyttsx3
import re

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def clean_text(event=None):
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Input Error", "Please enter some text.")
        return

    cleaned = re.sub(r'[^a-zA-Z\s\u263a-\U0001f645]', '', text)
    result_label.config(text=f"Cleaned: {cleaned}", fg="darkblue")
    speak(cleaned)
    root.after(3000, reset)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Text Cleaner (Letters Only)")
root.geometry("520x250")
root.resizable(False, False)

tk.Label(root, text="Enter text to clean:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center", width=50)
entry.pack(pady=5)
entry.bind("<Return>", clean_text)

tk.Button(root, text="Clean Text", font=("Arial", 12), command=clean_text).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=480)
result_label.pack(pady=10)

entry.focus()
root.mainloop()
