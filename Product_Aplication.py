
import sqlite3  
from tkinter import ttk
from tkinter import *


class Product:
    def __init__(self,window):
        self.wind =window
        self.wind.title('Product aplication')
        #creating Frame conteiner
        frame= LabelFrame(self.wind, text="Register a new product")
        frame.grid(row=0, column=0, columnspan=3, pady=20) 
        
       #Creating Name Input
        Label(frame, text= 'Name: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1) 

        # Name Input
        Label(frame, text= 'Price: ').grid(row=2, column=0)
        self.price= Entry(frame)
        self.price.grid(row=2, column=1)  

        # Button Add Product 
        Button(frame,text='Save Product').grid(row=3, columnspan=2, sticky= W+E) 
        
         # Button Delete Product 
        # Button(frame,text='Delete Product').grid(row=3, columnspan=2, sticky= W+E)  

        # Tabel
        self.tree =ttk.Treeview(height=10, columns=2) 
        self.tree.grid(row=4, column=0,columnspan=2) 
        self.tree.heading('#0', text = "Name", anchor=CENTER)
        self.tree.heading('#1', text = "Price", anchor=CENTER)

if __name__ == "__main__": 
    window = Tk()
    application = Product(window)
    window.mainloop()
