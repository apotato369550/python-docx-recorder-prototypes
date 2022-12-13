from docxtpl import DocxTemplate
doc = DocxTemplate("templates/po_template.docx")

invoice_number = input("Please input your invoice number: ") #convert using str()
sold_to = input("Please input name of customer: ")
tin = input("Please input TIN: ")
date = input("Please input date of transaction (mm/dd/yy): ")
terms = input("Please input terms of the purchase order: ")
address = input("Please input address of purchaser: ")
osca_pwd_id = input("Please input OSCA/PWD ID if applicable: ")
business_style = input("Please input business style: ")

sales_table_rows = []

while True:
    article = input("Please enter item name: ")
    unit = input("Please enter item unit: ")
    quantity = input("Please enter item quantity: ")
    while not quantity.isdigit() or int(quantity) <= 0:
        quantity = input("Please enter a valid quantity greater than 0:")


    while True:
        unit_price = input("Please enter item unit price: ")
        try:
            float(unit_price)
            break
        except ValueError:
            print('Please enter a valid unit price')



    amount = float(quantity) * float(unit_price)

    item = {}

    print("Article: " + article)
    print("Unit: " + unit)
    print("Quantity: " + quantity)
    print("Unit Price: " + unit_price)
    print("Amount: " + str(amount))

    add_item = input("Do you wish to add this item to the doc? (y/n) ")

    while add_item != "y" and add_item != "n":
        add_item = input("Please enter a valid input: ")
    
    if add_item == "y":
        item["quantity"] = quantity
        item["unit"] = unit
        item["articles"] = article
        item["unit_price"] = unit_price
        item["amount"] = str(amount)

        sales_table_rows.append(item)

    cont = input("Do you wish to continue adding another item? (y/n) ")

    while add_item != "y" and add_item != "n":
        cont = input("Please enter a valid input: ")
    
    if cont == "n":
        break


print("Invoice number: " + invoice_number)
print("Sold to: " + sold_to)
print("Date: " + date)
print("Terms: " + terms)
print("Address: " + address)
print("OSCA/PWD ID: " + osca_pwd_id)
print("Business Style: " + business_style)

total_sales = 0
discount = 0
withholding_tax = 0

for item in sales_table_rows:
    total_sales += float(item["amount"])

while True:
    discount = input("Please input SC/PWD discount rate in decimal (0.9 = 90%, 0.1 = 10%, etc.): ")
    try:
        discount = float(discount)
        break
    except ValueError:
        print('Please enter a valid discount rate.')

while True:
    withholding_tax = input("Please input Withholding tax rate in decimal (0.9 = 90%, 0.1 = 10%, etc.): ")
    try:
        withholding_tax = float(discount)
        break
    except ValueError:
        print('Please enter a valid Withholding tax rate.')

discount = total_sales * discount
total_amount = total_sales - discount
withholding_tax = total_amount * withholding_tax
total_amount_due = total_amount - withholding_tax

context = {
    "invoice_number": invoice_number,
    "sold_to": sold_to,
    "date": date,
    "tin": tin,
    "terms": terms,
    "address": address,
    "osca_pwd_id": osca_pwd_id,
    "business_style": business_style,
    "sales_table_rows": sales_table_rows,
    "total_sales": str(total_sales),
    "sc_pwd_discount": str(discount),
    "total_amount": total_amount,
    "withholding_tax": withholding_tax,
    "total_amount_due": total_amount_due
}

doc.render(context)
doc.save('output/sample.docx')
