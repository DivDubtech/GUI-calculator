import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("600x600")
        self.configure(bg="white")

        self.expression =""
        self.input_text =tk.StringVar()

        input_frame=self.create_input_frame()
        input_frame.pack()

        button_frame=self.create_button_frame()
        button_frame.pack()

    def create_input_frame(self):
        frame=tk.Frame(self,bg="green")
        input_field=tk.Entry(
            frame,textvariable=self.input_text,font=('arial',18,'bold'), bd=10, insertwidth=4, width=14, borderwidth=4,
            bg="grey",fg="black"
        )
        input_field.grid(row=0,column=0)
        input_field.pack(ipady=10)
        return frame

    def create_button_frame(self):
        frame=tk.Frame(self,bg="grey")

        buttons = [
            ('7', 1, 0),('8', 1, 1),('9', 1, 2),('/', 1, 3),
            ('4', 2, 0),('5', 2, 1),('6', 2, 2),('*', 2, 3),
            ('1', 3, 0),('2', 3, 1),('3', 3, 2),('-', 3, 3),
            ('C', 4, 0),('0', 4, 1),('=', 4, 2),('+', 4, 3),
        ]

        for (text, row, column)in buttons:
            if text =='=':
                color ="green"  # Green for '='
            elif text in {'/','*','-','+'}:
                color ="orange"  # Orange for operators
            elif text =='C':
                color ="red"  # Red for clear
            else:
                color ="white"  # White for numbers

            button =tk.Button(
                frame,text=text,font=('arial',18,'bold'), fg="black", bg=color, height=3, width=9,
                command=lambda txt=text: self.on_button_click(txt)
            )
            button.grid(row=row,column=column)

        return frame

    def on_button_click(self,char):
        if char =='C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result =str(eval(self.expression))
                self.input_text.set(result)
                self.expression =result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app =Calculator()
    app.mainloop()
