# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import DataModel as Model

def main():
    root = tk.Tk()
    root.title("Tkinter MVC App")
    
    model = Model()
    view = View(root)
    controller = Controller(model,view)
    
    root.mainloop()

if __name__ == "__main__":
    main()
