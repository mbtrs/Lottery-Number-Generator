import numpy as np

def lot_numbers():
    list = np.random.randint(low=1, high=49, size=6)
    list.sort()
    l2.config(text = list)

import tkinter as tk

window = tk.Tk()
window.geometry("325x200")
window.config(bg="#fff")
window.resizable(width=False,height=False)
window.title('Lottery Number Generator')


l1 = tk.Label(text="Lottery Number Generator",font=("Arial",20),bg="Black",fg="White")

b1 = tk.Button(text="Click here to generate lottery numbers",font=("Arial",15),bg="#A3E4D7",command=lot_numbers)

l2 = tk.Label(bg="#fff",fg="#000",font=("Arial",30),text="")

l1.place(x=25,y=20)
b1.place(x=15,y=80)
l2.place(x=15,y=130)

window.mainloop()
