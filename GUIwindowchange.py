import tkinter as tk




def newWindow(self):
    newWindow = tk.Toplevel()
    newWindow.title("new window")
    newWindow.geometry('400x400')
    newWindow.config(background="red")

window = tk.Tk()

label = tk.Label(window,text="click to go to next page")
label.pack()

button = tk.Button(window,text="press")
def click():
    newWindow()
    
button.bind('<button-1>',newWindow)
    
button.pack()



window.mainloop()
