import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry

class po_maker(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.max_width = 700
        self.max_height = 900

        self.title("PO/Receipt Recorder")
        self.geometry(str(self.max_width) + "x" + str(self.max_height))
        self.resizable(False, False)

        self.make_user_interface()
        self.mainloop()

        return

    def make_user_interface(self):
        # making components

        # frame
        self.user_interface_frame = Frame(self, width=self.max_width, height=self.max_height)

        # labels
        self.po_maker_label = Label(self.user_interface_frame, text="PO/Receipt Recorder/Maker", font=("Courier", 38, "bold"))
        self.invoice_number_label = Label(self.user_interface_frame, text="Invoice Number: ", font=("Arial", 14, "bold"))
        self.customer_name_label = Label(self.user_interface_frame, text="Customer Name: ")
        self.tin_label = Label(self.user_interface_frame, text="TIN: ")
        self.date_label = Label(self.user_interface_frame, text="Date of transaction: ")
        self.terms_label = Label(self.user_interface_frame, text="Terms: ")
        self.address_label = Label(self.user_interface_frame, text="Address: ")
        self.business_style_label = Label(self.user_interface_frame, text="Business Style: ")
        self.sc_pwd_id_label = Label(self.user_interface_frame, text="SC/PWD Discount ID: ")
        self.sc_pwd_discount_label = Label(self.user_interface_frame, text="SC/PWD Discount Rate (%) (in decimal): ")
        self.withholding_tax_label = Label(self.user_interface_frame, text="Withholding Tax Rate (%) (in decimal): ")

        # entries
        self.invoice_number_entry = Entry(self.user_interface_frame, width=20, borderwidth=5)
        self.customer_name_entry = Entry(self.user_interface_frame, width=40, borderwidth=5)
        self.tin_entry = Entry(self.user_interface_frame, width=20, borderwidth=5)
        self.date_entry = DateEntry(self.user_interface_frame, width= 16, background= "magenta3", foreground= "white", bd=5, borderwidth=5)
        self.terms_entry = Entry(self.user_interface_frame, width=40, borderwidth=5)
        self.address_entry = Entry(self.user_interface_frame, width=40, borderwidth=5)
        self.business_style_entry = Entry(self.user_interface_frame, width=20, borderwidth=5)
        self.sc_pwd_id_entry = Entry(self.user_interface_frame, width=10, borderwidth=5)
        self.sc_pwd_discount_entry = Entry(self.user_interface_frame, width=10, borderwidth=5)
        self.withholding_tax_entry = Entry(self.user_interface_frame, width=10, borderwidth=5)

        # placing them in a grid
        self.user_interface_frame.pack()

        self.po_maker_label.grid(row=0, column=2, pady=15)

        #labels
        self.customer_name_label.grid(row=1, column=0)
        self.tin_label.grid(row=3, column=0)
        self.address_label.grid(row=5, column=0)
        self.business_style_label.grid(row=7, column=0)
        self.sc_pwd_discount_label.grid(row=9, column=0)

        self.date_label.grid(row=1, column=3)
        self.terms_label.grid(row=3, column=3)
        self.sc_pwd_discount_label.grid(row=5, column=3)
        self.withholding_tax_label.grid(row=7, column=3)
        self.invoice_number_label.grid(row=9, column=3)

        # entries
        self.customer_name_entry.grid(row=2, column=0)
        self.tin_entry.grid(row=4, column=0)
        self.address_entry.grid(row=6, column=0)
        self.business_style_entry.grid(row=8, column=0)
        self.sc_pwd_discount_label.grid(row=10, column=0)

        self.date_entry
        #figure out date entry:V

        return


if __name__ == "__main__":
    po_maker()