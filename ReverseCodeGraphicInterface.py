#_[N_F]_
import tkinter as tk

window = tk.Tk()


def click():
    message = str(box.get())
    final_message, n = '', len(message)
    x = 0
    while x < n:
        final_message += message[n - x - 1]
        x += 1
    label["text"] = final_message
    final_message = ''


button = tk.Button(window, width=40,
                   height=2, relief='solid',
                   text='Crypt | Decrypt', command=click)
button.place(x=5, y=100)

label = tk.Label(window, width=40,
                 height=2, relief='solid',
                 text='message', background='white')
label.place(x=5, y=200)

box = tk.Entry(window, width=47,relief='solid', font='calabri 12')
box.place(x=5, y=5)

window.title("Reverse Code")
window.geometry("300x300")
window.mainloop()
