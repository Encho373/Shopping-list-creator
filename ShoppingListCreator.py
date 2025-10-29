import tkinter as tk

window = tk.Tk()
window.title("ShoppingList")
window.geometry("200x250")

def add_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)

frame = tk.Frame(window)
frame.grid(row=0,column=0)

entry = tk.Entry(frame)
entry.grid(row=0,column=0)

entry.bind("<Return>", add_list)

button = tk.Button(frame,text="Add",command=add_list)
button.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="ew")

window.mainloop()
