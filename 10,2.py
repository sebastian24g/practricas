from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["juli", "esteban", "hernan"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de nombres de personas")
label.pack()
master.mainloop()