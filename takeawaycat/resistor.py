import tkinter as tk

class Resistor:
    color = ["black","brown","red","orange","yellow",
             "green","blue","violet","grey","white"]

    def __init__(self,c1,c2,c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.value = 0.0

    def setC1(self, c1):
        if c1 in Resistor.color:
            self.c1 = c1
        else:
            raise ValueError("Invalid color: {}".format(c1))

    def setC2(self, c2):
        if c2 in Resistor.color:
            self.c2 = c2
        else:
            raise ValueError("Invalid color: {}".format(c2))

    def setC3(self, c3):
        if c3 in Resistor.color:
            self.c3 = c3
        else:
            raise ValueError("Invalid color: {}".format(c3))

    def setValue(self):
        self.value = 0.0
        c1_index = Resistor.color.index(self.c1)
        c2_index = Resistor.color.index(self.c2)
        c3_index = Resistor.color.index(self.c3)
        self.value = (c1_index*10 + c2_index) * (10 ** c3_index)

    def getc1(self):
        return self.c1

    def getc2(self):
        return self.c2

    def getc3(self):
        return self.c3

    def getValue(self):
        return self.value

    def __str__(self):
        return f"Band 1: " + self.c1 + " Band 2: " + self.c2 + " Band 3: " + self.c3 + " Value: " + str(self.getValue())

r = Resistor()
# r.setC1("brown")
# r.setC2("black")
# r.setC3("orange")

print(r.__str__())




# def showans():
#     c1_value = c1.get()
#     c2_value = c2.get()
#     c3_value = c3.get()

#     try:
#         resistor.setC1(c1_value)
#         resistor.setC2(c2_value)
#         resistor.setC3(c3_value)
#         resistor.setValue(0.0)
#         label.config(text="Resistor value: " + str(resistor.getValue()))
#     except ValueError as e:
#         label.config(text=e.args[0])  # Access specific error message

# # Main window
# main_window = tk.Tk()
# main_window.geometry('400x400')
# main_window.config(background='grey')

# color1 = tk.Label(main_window, text="Enter first color:", background='red')
# color1.pack()
# c1 = tk.Entry(main_window)
# c1.pack()

# color2 = tk.Label(main_window, text="Enter second color:", background='red')
# color2.pack()
# c2 = tk.Entry(main_window)
# c2.pack()

# color3 = tk.Label(main_window, text="Enter third color:", background='red')
# color3.pack()
# c3 = tk.Entry(main_window)
# c3.pack()

# resistor = Resistor("brown","black","orange")
# resistor.setC1(c1=resistor.getc1())
# resistor.setC2(c2=resistor.getc2())
# resistor.setC3(c3=resistor.getc3())

# resistor.setValue()


# save_button = tk.Button(main_window, text="Submit", command=showans)
# save_button.pack()

# label = tk.Label(main_window, text="Answer will show here", background='white')
# label.pack()

# # Calling the class

# main_window.mainloop()
