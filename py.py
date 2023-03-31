import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

username_label = ttk.Label(window, text="username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)



username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)


password_label = ttk.Label(window, text="password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)



password_entry = ttk.Entry(window, show='+')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)


login_button = ttk.Button(window, text= "loguin")
login_button.grid(column=1, row=3, sticky= tkinter.E, padx=6, pady=6)
window.mainloop()