import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("Calculator Jra")

        self.label = tk.Label(self.root, text="Hello DIP01", font= ("Arial", 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=2, width=3, font= ("Arial", 12) )
        self.button.place(x=10, y=40)
    
        self.button = tk.Button(self.root, text="+/-", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=80, y=40)

        self.button = tk.Button(self.root, text="%", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=150, y=40)

        self.button = tk.Button(self.root, text="/", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=220, y=40)
        
        self.button = tk.Button(self.root, text="7", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=10, y=90)
        
        self.button = tk.Button(self.root, text="8", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=80, y=90)
        
        self.button = tk.Button(self.root, text="9", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=150, y=90)
        
        self.button = tk.Button(self.root, text="*", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=220, y=90)
        
        self.button = tk.Button(self.root, text="4", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=10, y=140)
        
        self.button = tk.Button(self.root, text="5", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=80, y=140)
        
        self.button = tk.Button(self.root, text="6", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=150, y=140)
        
        self.button = tk.Button(self.root, text="-", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=220, y=140)
        
        self.button = tk.Button(self.root, text="1", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=10, y=190)
        
        self.button = tk.Button(self.root, text="2", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=80, y=190)
        
        self.button = tk.Button(self.root, text="3", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=150, y=190)
        
        self.button = tk.Button(self.root, text="+", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=220, y=190)
        
        self.button = tk.Button(self.root, text="0", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=70, y=240)

        self.button = tk.Button(self.root, text=".", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=150, y=240)

        self.button = tk.Button(self.root, text="=", height=2, width=3, font= ("Arial", 12))
        self.button.place(x=220, y=240)

        self.root.mainloop()

MyCalculator()