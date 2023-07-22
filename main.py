import tkinter as tk
from tkinter import messagebox
from pyurlx import shorten

def shorten_link():
    long_url = entry_long_url.get()

    try:
        short_url = shorten.shorten(long_url)
        entry_short_url.delete(0, tk.END)
        entry_short_url.insert(0, short_url)
        
     
        listbox_links.insert(tk.END, (long_url, short_url))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_link():
    short_url = entry_short_url.get()
    root.clipboard_clear()
    root.clipboard_append(short_url)
    messagebox.showinfo("Copied", "Link copied to clipboard!")

def open_copyable_link(event):
    selected_index = listbox_links.curselection()
    if selected_index:
        selected_item = listbox_links.get(selected_index[0])
        original_url, shortened_url = selected_item
        new_window = tk.Toplevel(root)
        new_window.title("Copyable Link")
        
        def copy_to_clipboard():
            new_window.clipboard_clear()
            new_window.clipboard_append(shortened_url)
            messagebox.showinfo("Copied", "Link copied to clipboard!")
            new_window.destroy()
        
        label_original_url = tk.Label(new_window, text=f"Original URL: {original_url}")
        label_original_url.pack(pady=5)
        
        label_shortened_url = tk.Label(new_window, text=f"Shortened URL: {shortened_url}")
        label_shortened_url.pack(pady=5)
        
        btn_copy_to_clipboard = tk.Button(new_window, text="Copy Link", command=copy_to_clipboard)
        btn_copy_to_clipboard.pack(pady=10)

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


listbox_links = tk.Listbox(root, width=50, height=10)
listbox_links.pack(pady=5, padx=10, side=tk.RIGHT, fill=tk.BOTH)
listbox_links.bind("<Double-Button-1>", open_copyable_link)

root.mainloop()

