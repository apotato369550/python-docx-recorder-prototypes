from tkinter import *
from tkinter import messagebox as mb

# during actual implementation, have an item class and a catalog class
# a catalog holds items and methods that deal w/ items
# items hold quantity, article, and etc.

class Item:
    def __init__(self, quantity, article, unit, unit_price):
        self.quantity = quantity
        self.article = article
        self.unit = unit
        self.unit_price = unit_price
        self.amount = quantity * unit_price
        pass

items = []


root = Tk()
root.title("Listbox Columns")

max_width = 700
max_height = 500

root.geometry(str(max_width) + "x" + str(max_height))
root.resizable(False, False)

main_title_label = Label(root, text="Item Adder")
main_title_label.grid(row=0, column=0, columnspan=2)

quantity_label = Label(root, text="Quantity: ")
quantity_entry = Entry(root, width=40)
quantity_label.grid(row=1, column=0)
quantity_entry.grid(row=2, column=0)


unit_price_label = Label(root, text="Unit Price: ")
unit_price_entry = Entry(root, width=40)
unit_price_label.grid(row=1, column=1)
unit_price_entry.grid(row=2, column=1)

unit_label = Label(root, text="Unit (pcs., kgs, boxes, etc.): ")
unit_entry = Entry(root, width=40)
unit_label.grid(row=3, column=0)
unit_entry.grid(row=4, column=0)

article_label = Label(root, text="Article: ")
article_entry = Entry(root, width=40)
article_label.grid(row=3, column=1)
article_entry.grid(row=4, column=1)

item_textbox = Text(root, width=40, height=20)
item_textbox.config(state=DISABLED)
item_textbox.grid(row=6, column=1, rowspan=4)

def display_item(listbox):
    # clear listbox, add newlines
    selected_index = listbox.curselection()[0]
    quantity = items[selected_index].quantity
    article = items[selected_index].article
    unit = items[selected_index].unit
    unit_price = items[selected_index].unit_price
    amount = items[selected_index].amount
    item_textbox.config(state=NORMAL)
    item_textbox.delete(1.0, END)
    item_textbox.insert(END, "Item Quantity: " + str(quantity) + "\n")
    item_textbox.insert(END, "Article: " + article + "\n")
    item_textbox.insert(END, "Unit: " + str(unit) + "\n")
    item_textbox.insert(END, "Unit Price: " + str(unit_price) + "\n")
    item_textbox.insert(END, "Amount: " + str(amount) + "\n")
    item_textbox.config(state=DISABLED)


def display_item_callback(event):
    print("Woot")
    display_item(event.widget)

item_listbox = Listbox(root, width=40, height=20, selectmode="SINGLE")
item_listbox.bind("<<ListboxSelect>>", display_item_callback)
item_listbox.grid(row=6, column=0)





def update_items_list():
    item_listbox.delete(0, END)

    for item in items:
        option = str(item.article)
        item_listbox.insert("end", option)

def add_item():
    quantity = quantity_entry.get()
    unit_price = unit_price_entry.get()
    unit = unit_entry.get()
    article = article_entry.get()

    if not quantity or not unit_price or not unit or not article:
        mb.showerror("Empty Fields", "Please make sure all fields are filled out.")
        return


    try:
        quantity = int(quantity)
        if quantity <= 0:
            mb.showerror("Quantity equal to 0", "Please enter a quantity greater than 0.")
            return
    except:
        mb.showerror("Invalid Quantity", "Please enter a valid quantity greater than 0. Omit all nondigit characters in the input field.")
        return

    try:
        unit_price = float(unit_price)
        if unit_price <= 0:
            mb.showerror("Unit Price equal to 0", "Please enter a unit price greater than 0.")
            return
    except:
        mb.showerror("Invalid Unit Price", "Please enter a valid unit price greater than 0. Omit all nondigit characters in the input field.")
        return

    for item in items:
        if item.article == article:
            mb.showerror("Article already exists", "That article already exists in the catalog. Please delete the pre-existing article and create a new one if you wish to make changes.")
            return

    item = Item(quantity, article, unit, unit_price)
    items.append(item)
    print("Items now in list:")
    for item in items:
        print(item)
    update_items_list()

    return

def delete_item():
    index = item_listbox.curselection()[0]
    print(index)
    item_listbox.delete(index)
    items.pop(index)
    print("Items now in list:")
    for item in items:
        print(item)
    update_items_list()
    return

add_item_button = Button(root, text="Add Item", command=add_item)
add_item_button.grid(row=5, column=0)

delete_item_button = Button(root, text="Delete Item", command=delete_item)
delete_item_button.grid(row=5, column=1)


root.mainloop()
