import tkinter as tk
#creating window
window = tk.Tk()
window.title("Practical  GUI")
window.geometry('400x400')
window.config(background="blue")

#creating label and modify attributes
label = tk.Label(window,text="click me",pady="20")

#changing background color
label.config(background="white")
label.config(width="100")

label.pack()

#textfield
name = tk.Entry(window)
name.pack()

#button
button = tk.Button(window,text="click me")
def button_click(self):
    label.config(text=name.get())

button.bind('<Button-1>',button_click)
button.pack()


window.mainloop()
