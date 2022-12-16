import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import Calendar

class POMaker(tk.Tk):
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
        
        def get_date():
            self.selected_date_label.config(text="Selected Date: " + self.date_entry.get_date())
            self.selected_date = self.date_entry.get_date()
        # frame
        self.user_interface_frame = Frame(self, width=self.max_width, height=self.max_height)
        self.user_interface_frame.pack()

        # RE-GRID ALL OF THE TKINTER WIDGETS t_t
        self.po_maker_label = Label(self.user_interface_frame, text="Receipt Maker", font=("Courier", 20, "bold"))
        self.po_maker_label.grid(row=0, column=0, pady=15, columnspan=2)

        self.invoice_number_label = Label(self.user_interface_frame, text="Invoice Number: ")
        self.invoice_number_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        # self.invoice_number_label.grid(row=7, column=3)
        #self.invoice_number_entry.grid(row=8, column=3)


        self.customer_name_label = Label(self.user_interface_frame, text="Customer Name: ")
        self.customer_name_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        # self.customer_name_label.grid(row=1, column=0)
        # self.customer_name_entry.grid(row=2, column=0)

        self.tin_label = Label(self.user_interface_frame, text="TIN: ")
        self.tin_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        # self.tin_label.grid(row=3, column=0)
        # self.tin_entry.grid(row=4, column=0)

        self.date_label = Label(self.user_interface_frame, text="Date of transaction: ")
        self.date_entry = Calendar(self.user_interface_frame, selectmode="day", year=2022, month=1, date=1)
        self.selected_date_label = Label(self.user_interface_frame, text="Selected Date: ")
        self.select_date_button = Button(self.user_interface_frame, text="Select Date", command=get_date)
        #self.date_label.grid(row=9, column=3)
        #self.date_entry.grid(row=11, column=3)
        #self.selected_date_label.grid(row=12, column=3)
        #self.select_date_button.grid(row=14, column=3)

        self.terms_label = Label(self.user_interface_frame, text="Terms: ")
        self.terms_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        #self.terms_label.grid(row=1, column=3)
        #self.terms_entry.grid(row=2, column=3)

        self.osca_pwd_id_label = Label(self.user_interface_frame, text="OSCA/PWD ID (if applicable): ")
        self.osca_pwd_id_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        #self.osca_pwd_id_label.grid(row=3, column=3)
        #self.osca_pwd_id_entry.grid(row=4, column=3)

        self.address_label = Label(self.user_interface_frame, text="Address: ")
        self.address_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        #self.address_label.grid(row=5, column=0)
        #self.address_entry.grid(row=6, column=0)

        self.business_style_label = Label(self.user_interface_frame, text="Business Style: ")
        self.business_style_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        #self.business_style_label.grid(row=7, column=0)
        #self.business_style_entry.grid(row=8, column=0)

        self.sc_pwd_discount_label = Label(self.user_interface_frame, text="SC/PWD Discount Rate (%) (in decimal): ")
        self.sc_pwd_discount_entry = Entry(self.user_interface_frame, width=15, borderwidth=5)
        #self.sc_pwd_discount_label.grid(row=9, column=0)
        #self.sc_pwd_discount_entry.grid(row=10, column=0)

        self.withholding_tax_label = Label(self.user_interface_frame, text="Withholding Tax Rate (%) (in decimal): ")
        self.withholding_tax_entry = Entry(self.user_interface_frame, width=15, borderwidth=5)
        #self.withholding_tax_label.grid(row=5, column=3)
        #self.withholding_tax_entry.grid(row=6, column=3)



if __name__ == "__main__":
    po_maker = POMaker()