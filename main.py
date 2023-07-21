import tkinter as tk
from tkinter import messagebox
from pyurlx import shorten

def shorten_link():
    long_url = entry_long_url.get()

    try:
        short_url = shorten.shorten(long_url)
        entry_short_url.delete(0, tk.END)
        entry_short_url.insert(0, short_url)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_link():
    short_url = entry_short_url.get()
    root.clipboard_clear()
    root.clipboard_append(short_url)
    messagebox.showinfo("Copied", "Link copied to clipboard!")

root = tk.Tk()
root.title("Link Shortener")

label_long_url = tk.Label(root, text="Long URL:")
label_long_url.pack(pady=5)

entry_long_url = tk.Entry(root, width=50)
entry_long_url.pack(pady=5)

label_short_url = tk.Label(root, text="Short URL:")
label_short_url.pack(pady=5)

entry_short_url = tk.Entry(root, width=50)
entry_short_url.pack(pady=5)

btn_shorten = tk.Button(root, text="Shorten", command=shorten_link)
btn_shorten.pack(pady=10)

btn_copy = tk.Button(root, text="Copy Link", command=copy_link)
btn_copy.pack(pady=10)

root.mainloop()

