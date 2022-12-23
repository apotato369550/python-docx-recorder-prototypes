import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from Item import Item
from tkinter import messagebox as mb
from docxtpl import DocxTemplate


class POMaker(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.max_width = 700
        self.max_height = 950

        self.title("PO/Receipt Recorder")
        self.geometry(str(self.max_width) + "x" + str(self.max_height))
        self.resizable(False, False)

        # idea to modularize/make oop make_user_interface():
        # method to create frames for each menu, each frame being its own object
        # under each frame, submodules that can be used/reaused as classes (datepicker, itemadder, etc.)

        self.items = []

        self.make_user_interface()
        self.make_date_picker()
        self.make_article_adder()
        
        record_receipt_button = Button(self.user_interface_frame, text="Record Receipt", command=self.record_receipt, font=("Courier", 15, "bold"))
        record_receipt_button.grid(row=25, column=0, pady=4, columnspan=2)

        self.mainloop()

        return

    def make_user_interface(self):
        # making components
        
        # frame
        self.user_interface_frame = Frame(self, width=self.max_width, height=self.max_height)
        self.user_interface_frame.pack()

        # RE-GRID ALL OF THE TKINTER WIDGETS t_t
        self.po_maker_label = Label(self.user_interface_frame, text="Receipt Maker", font=("Courier", 30, "bold"))
        self.po_maker_label.grid(row=0, column=0, pady=5, columnspan=2)

        self.basic_info_label = Label(self.user_interface_frame, text="Basic Info", font=("Arial", 20, "bold"))
        self.basic_info_label.grid(row=1, column=0, pady=5, columnspan=2)

        self.invoice_number_label = Label(self.user_interface_frame, text="Invoice Number: ")
        self.invoice_number_entry = Entry(self.user_interface_frame, width=30, borderwidth=5)
        self.invoice_number_label.grid(row=2, column=0, columnspan=2)
        self.invoice_number_entry.grid(row=3, column=0, columnspan=2)


        self.customer_name_label = Label(self.user_interface_frame, text="Customer Name: ")
        self.customer_name_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.customer_name_label.grid(row=4, column=0, padx=7)
        self.customer_name_entry.grid(row=5, column=0, padx=7)

        self.tin_label = Label(self.user_interface_frame, text="TIN: ")
        self.tin_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.tin_label.grid(row=4, column=1, padx=7)
        self.tin_entry.grid(row=5, column=1, padx=7)

        self.terms_label = Label(self.user_interface_frame, text="Terms: ")
        self.terms_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.terms_label.grid(row=6, column=0, padx=7)
        self.terms_entry.grid(row=7, column=0, padx=7)

        self.osca_pwd_id_label = Label(self.user_interface_frame, text="OSCA/PWD ID (if applicable): ")
        self.osca_pwd_id_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.osca_pwd_id_label.grid(row=6, column=1, padx=7)
        self.osca_pwd_id_entry.grid(row=7, column=1, padx=7)

        self.address_label = Label(self.user_interface_frame, text="Address: ")
        self.address_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.address_label.grid(row=8, column=0, padx=7)
        self.address_entry.grid(row=9, column=0, padx=7)

        self.business_style_label = Label(self.user_interface_frame, text="Business Style: ")
        self.business_style_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.business_style_label.grid(row=8, column=1, padx=7)
        self.business_style_entry.grid(row=9, column=1, padx=7)

        self.sc_pwd_discount_label = Label(self.user_interface_frame, text="SC/PWD Discount Rate (%) (in decimal): ")
        self.sc_pwd_discount_entry = Entry(self.user_interface_frame, width=20, borderwidth=5)
        self.sc_pwd_discount_label.grid(row=10, column=0)
        self.sc_pwd_discount_entry.grid(row=11, column=0)

        self.withholding_tax_label = Label(self.user_interface_frame, text="Withholding Tax Rate (%) (in decimal): ")
        self.withholding_tax_entry = Entry(self.user_interface_frame, width=20, borderwidth=5)
        self.withholding_tax_label.grid(row=10, column=1)
        self.withholding_tax_entry.grid(row=11, column=1)

    def make_date_picker(self):
        def get_date():
            self.selected_date_label.config(text="Selected Date: " + self.date_entry.get_date())
            self.selected_date = self.date_entry.get_date()

        self.date_picker = Label(self.user_interface_frame, text="Date Selection", font=("Arial", 20, "bold"))
        self.date_picker.grid(row=12, column=0, pady=5)

        self.date_entry = Calendar(self.user_interface_frame, selectmode="day", year=2022, month=1, date=1)
        self.selected_date_label = Label(self.user_interface_frame, text="Selected Date: ")
        self.select_date_button = Button(self.user_interface_frame, text="Select Date", command=get_date)
        self.date_entry.grid(row=14, column=0, rowspan=7)
        self.selected_date_label.grid(row=13, column=0, pady=5)
        self.select_date_button.grid(row=21, column=0)

    def make_article_adder(self):
        self.date_picker = Label(self.user_interface_frame, text="Add Items", font=("Arial", 20, "bold"))
        self.date_picker.grid(row=12, column=1, pady=5)

        self.quantity_label = Label(self.user_interface_frame, text="Quantity: ")
        self.quantity_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.quantity_label.grid(row=13, column=1)
        self.quantity_entry.grid(row=14, column=1)


        self.unit_price_label = Label(self.user_interface_frame, text="Unit Price: ")
        self.unit_price_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.unit_price_label.grid(row=15, column=1)
        self.unit_price_entry.grid(row=16, column=1)

        self.unit_label = Label(self.user_interface_frame, text="Unit (pcs., kgs, boxes, etc.): ")
        self.unit_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.unit_label.grid(row=17, column=1)
        self.unit_entry.grid(row=18, column=1)

        self.article_label = Label(self.user_interface_frame, text="Article: ")
        self.article_entry = Entry(self.user_interface_frame, width=45, borderwidth=5)
        self.article_label.grid(row=19, column=1)
        self.article_entry.grid(row=20, column=1)

        self.item_textbox_label = Label(self.user_interface_frame, text="Item List", font=("Arial", 13))
        self.item_textbox_label.grid(row=22, column=0, pady=5)

        self.item_listbox_label = Label(self.user_interface_frame, text="Item Description", font=("Arial", 13))
        self.item_listbox_label.grid(row=22, column=1, pady=5)

        self.item_textbox = Text(self.user_interface_frame, width=40, height=12, borderwidth=5)
        self.item_textbox.config(state=DISABLED)
        self.item_textbox.grid(row=23, column=1)

        def display_item(listbox):
            try:
                selected_index = listbox.curselection()[0]
            except:
                return
            quantity = self.items[selected_index].quantity
            article = self.items[selected_index].article
            unit = self.items[selected_index].unit
            unit_price = self.items[selected_index].unit_price
            amount = self.items[selected_index].amount
            self.item_textbox.config(state=NORMAL)
            self.item_textbox.delete(1.0, END)
            self.item_textbox.insert(END, "Item Quantity: " + str(quantity) + "\n")
            self.item_textbox.insert(END, "Article: " + article + "\n")
            self.item_textbox.insert(END, "Unit: " + str(unit) + "\n")
            self.item_textbox.insert(END, "Unit Price: " + str(unit_price) + "\n")
            self.item_textbox.insert(END, "Amount: " + str(amount) + "\n")
            self.item_textbox.config(state=DISABLED)


        def display_item_callback(event):
            display_item(event.widget)

        self.item_listbox = Listbox(self.user_interface_frame, width=40, height=12, selectmode="SINGLE", borderwidth=5)
        self.item_listbox.bind("<<ListboxSelect>>", display_item_callback)
        self.item_listbox.grid(row=23, column=0)

        def update_items_list():
            self.item_listbox.delete(0, END)

            for item in self.items:
                option = str(item.article)
                self.item_listbox.insert("end", option)

        def add_item():
            self.quantity = self.quantity_entry.get()
            self.unit_price = self.unit_price_entry.get()
            self.unit = self.unit_entry.get()
            self.article = self.article_entry.get()

            if not self.quantity or not self.unit_price or not self.unit or not self.article:
                mb.showerror("Item Adder: Empty Fields", "Please make sure all fields are filled out.")
                return


            try:
                self.quantity = int(self.quantity)
                if self.quantity <= 0:
                    mb.showerror("Item Adder: Quantity equal to 0", "Please enter a quantity greater than 0.")
                    return
            except:
                mb.showerror("Item Adder: Invalid Quantity", "Please enter a valid quantity greater than 0. Omit all nondigit characters in the input field.")
                return

            try:
                self.unit_price = float(self.unit_price)
                if self.unit_price <= 0:
                    mb.showerror("Item Adder: Unit Price equal to 0", "Please enter a unit price greater than 0.")
                    return
            except:
                mb.showerror("Item Adder: Invalid Unit Price", "Please enter a valid unit price greater than 0. Omit all nondigit characters in the input field.")
                return

            for item in self.items:
                if item.article == self.article:
                    mb.showerror("Item Adder: Article already exists", "That article already exists in the catalog. Please delete the pre-existing article and create a new one if you wish to make changes.")
                    return

            item = Item(self.quantity, self.article, self.unit, self.unit_price)
            self.items.append(item)
            print("Items now in list:")
            update_items_list()

            return

        def delete_item():
            try:
                self.index = self.item_listbox.curselection()[0]
            except:
                return
            self.item_listbox.delete(self.index)
            self.items.pop(self.index)
            print("Items now in list:")
            for item in self.items:
                print(item)
            update_items_list()

        self.add_item_button = Button(self.user_interface_frame, text="Add Item", command=add_item)
        self.add_item_button.grid(row=21, column=1)

        self.delete_item_button = Button(self.user_interface_frame, text="Delete Item", command=delete_item)
        self.delete_item_button.grid(row=24, column=0, pady=4)

    def record_receipt(self):
        self.invoice_number = self.invoice_number_entry.get()
        self.customer_name = self.customer_name_entry.get()
        self.tin = self.tin_entry.get()
        self.terms = self.terms_entry.get()
        self.osca_pwd_id = self.osca_pwd_id_entry.get()
        self.address = self.address_entry.get()
        self.business_style = self.business_style_entry.get()
        self.withholding_tax = self.withholding_tax_entry.get()
        self.sc_pwd_discount = self.sc_pwd_discount_entry.get()

        self.date = self.date_entry.get_date()

        if (not self.invoice_number or not self.customer_name or not self.tin or not self.terms 
        or not self.osca_pwd_id or not self.address or not self.business_style):
            mb.showerror("Basic Info: Empty Fields", "Please make sure all fields are filled out. Please type 'N/A' in any of the fields that do not apply")
            return

        
        try:
            self.sc_pwd_discount = float(self.sc_pwd_discount)
            if self.sc_pwd_discount >= 1 and self.sc_pwd_discount < 0:
                mb.showerror("Basic Info: SC/PWD Discount Rate", "Please enter a valid discount rate in decimal. The value entered must be less than 1, but greater than 0.")
                return
        except:
            mb.showerror("Basic Info: SC/PWD Discount Rate", "Please enter a valid discount rate. Omit all nondigit characters in the input field.")
            return
        
        try:
            self.withholding_tax = float(self.withholding_tax)
            if self.withholding_tax >= 1 and self.withholding_tax < 0:
                mb.showerror("Basic Info: Withholding Tax Rate", "Please enter a valid withholding tax rate in decimal. The value entered must be less than 1, but greater than 0.")
                return
        except:
            mb.showerror("Basic Info: Withholding Tax Rate", "Please enter a valid withholding tax rate. Omit all nondigit characters in the input field.")
            return
        
        if not self.date:
            mb.showerror("Date Selector: Empty Fields", "Please select a valid date.")
            return

        if not bool(self.items):
            mb.showerror("Item Adder: No Items Added", "Please add at least (1) item to the receipt.")
            return


        self.total_sales = 0
        self.sales_table_rows = []

        for item in self.items:
            self.total_sales += item.amount
            self.row = {}
            self.row["quantity"] = str(item.quantity)
            self.row["unit"] = item.unit
            self.row["articles"] = item.article
            self.row["unit_price"] = str(item.unit_price)
            self.row["amount"] = str(item.amount)
            self.sales_table_rows.append(self.row)

        self.sc_pwd_discount = self.total_sales * self.sc_pwd_discount
        self.total_amount = self.total_sales - self.sc_pwd_discount
        self.withholding_tax = self.total_amount * self.withholding_tax
        self.total_amount_due = self.total_amount - self.withholding_tax

        self.doc = DocxTemplate("templates/po_template.docx")

        self.context = {
            "invoice_number": self.invoice_number,
            "sold_to": self.customer_name,
            "date": self.date,
            "tin": self.tin,
            "terms": self.terms,
            "address": self.address,
            "osca_pwd_id": self.osca_pwd_id,
            "business_style": self.business_style,
            "sales_table_rows": self.sales_table_rows,
            "total_sales": str(self.total_sales),
            "sc_pwd_discount": str(self.sc_pwd_discount),
            "total_amount": self.total_amount,
            "withholding_tax": self.withholding_tax,
            "total_amount_due": self.total_amount_due
        }

        self.doc.render(self.context)
        self.doc.save("output/invoice_number_" + self.invoice_number + ".docx")

        self.items = []
        self.item_listbox.delete(0, END)
        self.item_textbox.delete(0, END)
        
        mb.showinfo("Receipt Successfully Created", "Receipt successfully created. Please check the '/output' folder for the finished receipt.")
        
        # test me

        # fix this part

        

        



if __name__ == "__main__":
    po_maker = POMaker()