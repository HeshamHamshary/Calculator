"""

BASIC CALCULATOR USING TKINTER AND MATH
BY HESHAM EL HAMSHARY

"""


import tkinter as tk
from math import *
π = pi

class MainApplication():
    """Main Calculator application"""
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.minsize(width=350, height= 500)

        # Binding application to keyboard buttons
        self.master.bind("<Key>", self.focus)

        # Centering window on screen

        windowWidth = self.master.winfo_reqwidth()
        windowHeight = self.master.winfo_reqheight()
        positionRight = int(self.master.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.master.winfo_screenheight()/3 - windowHeight/3)
        self.master.geometry(f"+{positionRight}+{positionDown}")


        # result field
        self.result_field = tk.Entry(self.master, font="Helvetica 18 bold", borderwidth=2, bg="#f7f7f7", justify="right")

        # Adding buttons
        self.advanced = tk.Button(self.master, text= "Adv", font="Helvetica 18", borderwidth=1, height=1, width = 4, command=self.advanced)
        self.zero = tk.Button(self.master, text="0", font="Helvetica 18 bold", borderwidth=1, height = 1, width =  4, bg="white", command=lambda:self.enter_to_field("zero"))
        self.decimal = tk.Button(self.master, text=".", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("decimal"))
        self.equal = tk.Button(self.master, text="=", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command = lambda:self.enter_to_field("equal"))
        self.one = tk.Button(self.master, text="1", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("one"))
        self.two = tk.Button(self.master, text="2", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("two"))
        self.three = tk.Button(self.master, text="3", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("three"))
        self.plus = tk.Button(self.master, text="+", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("plus"))
        self.four = tk.Button(self.master, text="4", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("four"))
        self.five = tk.Button(self.master, text="5", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("five"))
        self.six = tk.Button(self.master, text="6", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("six"))
        self.minus = tk.Button(self.master, text="–", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("minus"))
        self.seven = tk.Button(self.master, text="7", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("seven"))
        self.eight = tk.Button(self.master, text="8", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("eight"))
        self.nine = tk.Button(self.master, text="9", font="Helvetica 18 bold", borderwidth=1, height = 1, width = 4, bg="white", command=lambda:self.enter_to_field("nine"))
        self.multiply = tk.Button(self.master, text="*", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("multiply"))
        self.ce = tk.Button(self.master, text="CE", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("ce"))
        self.c = tk.Button(self.master, text="C", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("c"))
        self.backspace = tk.Button(self.master, text="⌫", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("backspace"))
        self.divide = tk.Button(self.master, text="/", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("divide"))
        self.info = tk.Button(self.master,text="ⓘ", font="Helvetica 18", borderwidth=1, height=1, width = 4, command=self.infoWin)
        self.sqrt = tk.Button(self.master, text="√", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("sqrt"))
        self.sqr = tk.Button(self.master, text="x²", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("sqr"))
        self.inverse = tk.Button(self.master, text="1/x", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("inverse"))

        """main_widgets = [self.result_field, self.advanced, self.zero, self.decimal,
                        self.equal, self.one, self.two, self.three, self.plus,
                        self.four, self.five, self.six, self.minus, self.seven,
                        self.eight, self.nine, self.multiply, self.ce, self.c,
                        self.backspace, self.divide, self.info, self.sqrt,
                        self.sqr, self.inverse]"""

        # Placing buttons in grid
        self.result_field.grid(row=0, column=1, columnspan=4, rowspan=2, ipadx=40, ipady=40, pady=25, sticky="nsew")
        self.advanced.grid(row=8, column=1, padx=2, pady=2, sticky="nsew")
        self.zero.grid(row=8, column=2, padx=2, pady=2, sticky="nsew")
        self.decimal.grid(row=8, column=3, padx=2, pady=2, sticky="nsew")
        self.equal.grid(row=8, column=4, padx=2, pady=2, sticky="nsew")
        self.one.grid(row=7, column=1, padx=2, pady=2, sticky="nsew")
        self.two.grid(row=7, column=2, padx=2, pady=2, sticky="nsew")
        self.three.grid(row=7, column=3, padx=2, pady=2, sticky="nsew")
        self.plus.grid(row=7, column=4, padx=2, pady=2, sticky="nsew")
        self.four.grid(row=6, column=1, padx=2, pady=2, sticky="nsew")
        self.five.grid(row=6, column=2, padx=2, pady=2, sticky="nsew")
        self.six.grid(row=6, column=3, padx=2, pady=2, sticky="nsew")
        self.minus.grid(row=6, column=4, padx=2, pady=2, sticky="nsew")
        self.seven.grid(row=5, column=1, padx=2, pady=2, sticky="nsew")
        self.eight.grid(row=5, column=2, padx=2, pady=2, sticky="nsew")
        self.nine.grid(row=5, column=3, padx=2, pady=2, sticky="nsew")
        self.multiply.grid(row=5, column=4, padx=2, pady=2, sticky="nsew")
        self.ce.grid(row=4, column=1, padx=2, pady=2, sticky="nsew")
        self.c.grid(row=4, column=2, padx=2, pady=2, sticky="nsew")
        self.backspace.grid(row=4, column=3, padx=2, pady=2, sticky="nsew")
        self.divide.grid(row=4, column=4, padx=2, pady=2, sticky="nsew")
        self.info.grid(row=3, column = 1, padx=2, pady=2, sticky="nsew")
        self.sqrt.grid(row=3, column=2, padx=2, pady=2, sticky="nsew")
        self.sqr.grid(row=3, column=3, padx=2, pady=2, sticky="nsew")
        self.inverse.grid(row=3, column=4, padx=2, pady=2, sticky="nsew")

        # Adding resizing configuration
        for n in range(9):
            self.master.rowconfigure(n, weight=3)
        for n in range(1, 5):
            self.master.columnconfigure(n, weight=3)


    def focus(self, event):
        """Focuses on result entry when keyboard is used"""
        if self.result_field.get() == "ERROR... press CE" and input != "ce" or event.keysym == "BackSpace":
            pass
        else:
            if self.result_field == self.result_field.focus_get():
                if event.keysym == "Return":
                    self.enter_to_field("equal")
                else:
                    pass
            else:
                self.result_field.focus()
                self.result_field.insert(len(self.result_field.get()), event.char)


    # define advanced calculator
    def advanced(self):
        """Activates advanced calculator mode"""
        if self.advanced.cget("text") == "Adv":
            self.advanced.config(text="Std")
            self.result_field.grid(row=0, column=0, columnspan=5, rowspan=2, ipadx=40, ipady=40, pady=25, sticky="nsew")
            self.info.grid(row=2, column=0, padx=2, pady=2)

            # Adding advanced operation buttons
            self.lparen = tk.Button(self.master, text="(", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("lparen"))
            self.rparen = tk.Button(self.master, text=")", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("rparen"))
            self.factorial = tk.Button(self.master, text="n!", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("factorial"))
            self.pi = tk.Button(self.master, text="π", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("pi"))
            self.tenp = tk.Button(self.master, text="10^", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("tenp"))
            self.rd = tk.Button(self.master, text="Deg", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=self.degrees_radians)
            self.log = tk.Button(self.master, text="log", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("log"))
            self.ln = tk.Button(self.master, text="ln", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("ln"))
            self.sin = tk.Button(self.master, text="sin", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("sin"))
            self.cos = tk.Button(self.master, text="cos", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("cos"))
            self.tan = tk.Button(self.master, text="tan", font="Helvetica 18", borderwidth=1, height = 1, width = 4, command=lambda:self.enter_to_field("tan"))


            # Placing advanced operation buttons
            self.lparen.grid(row=8, column=0, padx=2, pady=2, sticky="nsew")
            self.rparen.grid(row=7, column=0, padx=2, pady=2, sticky="nsew")
            self.factorial.grid(row=6, column=0, padx=2, pady=2, sticky="nsew")
            self.pi.grid(row=5, column=0, padx=2, pady=2, sticky="nsew")
            self.tenp.grid(row=4, column=0, padx=2, pady=2, sticky="nsew")
            self.rd.grid(row=3, column=0, padx=2, pady=2, sticky="nsew")
            self.log.grid(row=3, column = 1, padx=2, pady=2, sticky="nsew")
            self.ln.grid(row=2, column=1, padx=2, pady=2, sticky="nsew")
            self.sin.grid(row=2, column=2, padx=2, pady=2, sticky="nsew")
            self.cos.grid(row=2, column=3, padx=2, pady=2, sticky="nsew")
            self.tan.grid(row=2, column=4, padx=2, pady=2, sticky="nsew")

            # Adding resizing configuration
            self.master.columnconfigure(0, weight=3)


        elif self.advanced.cget("text") == "Std":
            self.advanced.config(text="Adv")
            self.result_field.grid(row=0, column=1, columnspan=4, rowspan=2, ipadx=40, ipady=40, pady=25, sticky="nsew")
            self.info.grid(row=3, column = 1, padx=2, pady=2, sticky="nsew")

            # Hide advanced operation buttons
            self.lparen.grid_remove()
            self.rparen.grid_remove()
            self.factorial.grid_remove()
            self.pi.grid_remove()
            self.tenp.grid_remove()
            self.rd.grid_remove()
            self.log.grid_remove()
            self.ln.grid_remove()
            self.sin.grid_remove()
            self.cos.grid_remove()
            self.tan.grid_remove()

            # Remove resizing configuration
            self.master.columnconfigure(0, weight=0)


    def calculate(self, exp):
        """calculates and returns result"""
        if len(self.result_field.get()) == 0:
            pass
        else:
            try:
                result = round(eval(exp), 10)
                self.result_field.delete(0, "end")
                self.result_field.insert(0, result)
            except:
                self.master.focus()
                self.result_field.delete(0, "end")
                self.result_field.insert(0, "ERROR... press CE")

    def degrees_radians(self):
        """Sets calculator to degrees or radians mode"""
        if self.rd.cget("text") == "Deg":
            self.rd.config(text="Rad")

        elif self.rd.cget("text") == "Rad":
            self.rd.config(text="Deg")



    def enter_to_field(self, input):
        """Shows numbers and signs on result field"""
        numbers = ["zero", "one", "two", "three", "four", "five", "six",
                     "seven", "eight", "nine"]
        if self.result_field.get() == "ERROR... press CE" and input != "ce":
            pass
        else:
            if input in numbers[:10]:
                # Numbers
                self.result_field.insert(len(self.result_field.get()), f"{numbers.index(input)}")
            elif input == "decimal":
                if len(self.result_field.get()) == 0 or self.result_field.get()[len(self.result_field.get()) - 1:] in ["+", "-", "*", "/", "."]:
                    self.result_field.insert(len(self.result_field.get()), "0.")
                else:
                    self.result_field.insert(len(self.result_field.get()), ".")
            elif input == "equal":
                self.calculate(self.result_field.get())
            elif input == "plus":
                if self.result_field.get()[len(self.result_field.get()) - 1:] in ["+", "-", "*", "/", "."]:
                    pass
                elif len(self.result_field.get()) == 0:
                    self.result_field.insert(0, "0+")
                else:
                    self.result_field.insert(len(self.result_field.get()),"+")
            elif input == "minus":
                if "." in self.result_field.get()[len(self.result_field.get()) - 1:]:
                    pass
                else:
                    self.result_field.insert(len(self.result_field.get()),"-")
            elif input == "multiply":
                if self.result_field.get()[len(self.result_field.get()) - 1:] in ["+", "-", "*", "/", "."]:
                    pass
                elif len(self.result_field.get()) == 0:
                    self.result_field.insert(0, "0*")
                else:
                    self.result_field.insert(len(self.result_field.get()),"*")
            elif input == "ce" or input == "c":
                self.result_field.delete(0, "end")
            elif input == "backspace":
                self.result_field.delete(len(self.result_field.get()) - 1, "end")
            elif input == "divide":
                if self.result_field.get()[len(self.result_field.get()) - 1:] in ["+", "-", "×", "/", "."]:
                    pass
                elif len(self.result_field.get()) == 0:
                    self.result_field.insert(0, "0/")
                else:
                    self.result_field.insert(len(self.result_field.get()), "/")
            elif input == "sqrt":
                self.calculate(f"sqrt({self.result_field.get()})")
            elif input == "sqr":
                self.calculate(f"{self.result_field.get()}**2")
            elif input == "inverse":
                self.calculate(f"1/{self.result_field.get()}")

            # Advanced operation inputs
            elif input == "lparen":
                self.result_field.insert(len(self.result_field.get()),"(")
            elif input == "rparen":
                self.result_field.insert(len(self.result_field.get()),")")
            elif input == "factorial":
                self.calculate(f"factorial({self.result_field.get()})")
            elif input == "pi":
                self.result_field.insert(len(self.result_field.get()),"π")
            elif input == "tenp":
                self.calculate(f"10**{self.result_field.get()}")
            elif input == "log":
                self.calculate(f"log({self.result_field.get()}, 10)")
            elif input == "ln":
                self.calculate(f"log({self.result_field.get()})")
            elif input == "sin":
                if self.rd.cget("text") == "Deg":
                    self.calculate(f"sin(radians({self.result_field.get()}))")
                elif self.rd.cget("text") == "Rad":
                    self.calculate(f"sin({self.result_field.get()})")
            elif input == "cos":
                if self.rd.cget("text") == "Deg":
                    self.calculate(f"cos(radians({self.result_field.get()}))")
                elif self.rd.cget("text") == "Rad":
                    self.calculate(f"cos({self.result_field.get()})")
            elif input == "tan":
                if self.rd.cget("text") == "Deg":
                    self.calculate(f"tan(radians({self.result_field.get()}))")
                elif self.rd.cget("text") == "Rad":
                    self.calculate(f"tan({self.result_field.get()})")

    def infoWin(self):
        """Displays window when info button is pressed"""
        info = tk.Toplevel(self.master)
        thanks = tk.Label(info, text="Thanks for using my calculator!\n", font="Helvetica 14 bold underline").pack()
        creator = tk.Label(info, text="Made by: Hesham El Hamshary\nPurpose: Tkinter and python practice\n", font="Helvetica 14").pack()
        exit = tk.Button(info, text="exit", font="Helvetica 18", borderwidth=3, bg= "#115fdd", fg= "white", height = 1, width = 5, command=lambda:info.destroy()).pack()

        # Centering window on screen

        windowWidth = info.winfo_reqwidth()
        windowHeight = info.winfo_reqheight()
        positionRight = int(info.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(info.winfo_screenheight()/3 - windowHeight/3)
        info.geometry(f"+{positionRight + 25}+{positionDown + 150}")


root = tk.Tk()
Calc = MainApplication(root)
root.mainloop()
