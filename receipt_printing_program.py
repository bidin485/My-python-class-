from tkinter import *

def print_receipt():
    # Get input values
    customer_name = name_entry.get()
    product_name = product_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    total = quantity * price

    # Create a receipt string
    receipt = f"Customer Name: {customer_name}\n"
    receipt += f"Product: {product_name}\n"
    receipt += f"Quantity: {quantity}\n"
    receipt += f"Price: ${price:.2f}\n"
    receipt += f"Total: ${total:.2f}"

    # Display the receipt
    receipt_label.config(text=receipt)

root = Tk()
root.title("Receipt Printer")


# Create input fields
name_label = Label(root, text="Customer Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

product_label = Label(root, text="Product Name:")
product_label.pack()
product_entry = Entry(root)
product_entry.pack()

quantity_label = Label(root, text="Quantity:")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()

price_label = Label(root, text="Price:")
price_label.pack()
price_entry = Entry(root)
price_entry.pack()

# Create a button to print the receipt
print_button = Button(root, text="Print Receipt", command=print_receipt)
print_button.pack()

# Create a label to display the receipt
receipt_label = Label(root, text="")
receipt_label.pack()

root.mainloop()
