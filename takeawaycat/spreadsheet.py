class Cell:
    def __init__(self, content, row, column):
        self.content = content
        self.row = row
        self.column = column

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def evaluate(self):
        if isinstance(self.content, Formula):
            return self.content.evaluate()
        else:
            return self.content

class Formula:
    def __init__(self, op, operand1, operand2,finalvalue):
        self.op = op
        self.operand1 = operand1
        self.operand2 = operand2
        self.finalvalue = finalvalue
        
        
# The evaluate() function is a method of the Formula class. It is responsible for evaluating the formula in the operand1 and operand2 fields of the Formula object and returning the result.

    def evaluate(self):
        if isinstance(self.operand1, Cell):
            #checks if operand1 is an instance of the cell class
            operand1_value = self.operand1.evaluate()
        else:
            operand1_value = self.operand1

        if isinstance(self.operand2, Cell):
            operand2_value = self.operand2.evaluate()
        else:
            operand2_value = self.operand2

        if self.op == '+':
            finalvalue = str(operand1_value) + str(operand2_value)
            return finalvalue
        elif self.op == '-':
            finalvalue =  str(operand1_value) - str(operand2_value)
            return finalvalue
        elif self.op == '*':
            finalvalue =  str(operand1_value) * str(operand2_value)
            return finalvalue
        elif self.op == '/':
            finalvalue =  str(operand1_value)/ str(operand2_value)
            return finalvalue
        else:
            raise ValueError(f"Invalid formula operation: {self.op}")

class Spreadsheet:
    def __init__(self, rows, columns):
        self.cells = [[None for _ in range(columns)] for _ in range(rows)]

    def get_cell(self, row, column):
        return self.cells[row][column]

    def set_cell_content(self, row, column, content):
        self.cells[row][column] = Cell(content, row, column)

    def evaluate_all(self):
        for row in range(len(self.cells)):
            for column in range(len(self.cells[0])):
                self.cells[row][column].evaluate()

# Create a new spreadsheet with 10 rows and 5 columns
spreadsheet = Spreadsheet(10, 5)

# Set the content of cell A1 to the string "Hello"
spreadsheet.set_cell_content(0, 0, "Hello")

# Set the content of cell B1 to the number 10
spreadsheet.set_cell_content(0, 1, 10)

# Set the content of cell C1 to a formula that adds the contents of cells A1 and B1
spreadsheet.set_cell_content(0, 2, Formula('+', spreadsheet.get_cell(0, 0), spreadsheet.get_cell(0, 1),0))

# Evaluate all of the formulas in the spreadsheet
spreadsheet.evaluate_all()

# Print the content of cell C1
print(spreadsheet.get_cell(0, 2).get_content())
