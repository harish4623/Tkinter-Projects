import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connect to MySQL database on WAMP server
db = mysql.connector.connect(
    host="localhost",          # WAMP server host
    user="root",               # Default MySQL username
    password="",               # Default MySQL password (empty)
    database="product_database"  # Your MySQL database name
)
cursor = db.cursor()

# Create the products table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    name VARCHAR(255) PRIMARY KEY,
                    price DECIMAL(10, 2),
                    qty INT,
                    total DECIMAL(10, 2))''')
db.commit()

def calculate_total(price, qty):
    """Calculate the total price of a product."""
    return price * qty

def add_product():
    """Add a new product to the database."""
    name = entry_name.get()
    try:
        price = float(entry_price.get())
        qty = int(entry_qty.get())
        if not name or price < 0 or qty < 0:
            raise ValueError("Invalid input")

        total = calculate_total(price, qty)
        cursor.execute("INSERT INTO products (name, price, qty, total) VALUES (%s, %s, %s, %s)", (name, price, qty, total))
        db.commit()
        messagebox.showinfo("Success", f"Product '{name}' added successfully!")
        clear_entries()
        view_all_products()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid inputs!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

def view_all_products():
    """Display all products in the text widget."""
    text_display.config(state=tk.NORMAL)  # Make text widget editable to update content
    text_display.delete(1.0, tk.END)  # Clear previous contents of the text widget

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    if rows:
        output = "{:^20} {:^10} {:^10} {:^10}\n".format("Name", "Price", "Qty", "Total")
        output += "-"*50 + "\n"
        for row in rows:
            output += "{:^20} {:^10} {:^10} {:^10}\n".format(row[0], row[1], row[2], row[3])
        text_display.insert(tk.END, output)
    else:
        text_display.insert(tk.END, "No products found.")
    
    text_display.config(state=tk.DISABLED)  # Make text widget read-only after updating content

def update_product():
    """Update an existing product in the database."""
    name = entry_name.get()
    try:
        price = float(entry_price.get())
        qty = int(entry_qty.get())
        if not name or price < 0 or qty < 0:
            raise ValueError("Invalid input")

        total = calculate_total(price, qty)
        cursor.execute("UPDATE products SET price=%s, qty=%s, total=%s WHERE name=%s", (price, qty, total, name))
        db.commit()
        messagebox.showinfo("Success", f"Product '{name}' updated successfully!")
        clear_entries()
        view_all_products()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid inputs or check if the product exists!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

def delete_product():
    """Delete a product from the database."""
    name = entry_name.get()
    try:
        cursor.execute("DELETE FROM products WHERE name=%s", (name,))
        db.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Product '{name}' deleted successfully!")
        else:
            messagebox.showinfo("Info", f"Product '{name}' not found!")
        clear_entries()
        view_all_products()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database error: {err}")

def clear_entries():
    """Clear input fields."""
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

# Tkinter window setup
root = tk.Tk()
root.title("Product Database Management")
root.configure(bg="lightblue")  # Set the background color for the window

# Center the window
root.geometry('500x450')

# Create input fields
ttk.Label(root, text="Product Name:", background="lightblue").place(x=20, y=30, anchor="w")
entry_name = ttk.Entry(root)
entry_name.place(x=150, y=30, width=200)

ttk.Label(root, text="Product Price:", background="lightblue").place(x=20, y=70, anchor="w")
entry_price = ttk.Entry(root)
entry_price.place(x=150, y=70, width=200)

ttk.Label(root, text="Product Quantity:", background="lightblue").place(x=20, y=110, anchor="w")
entry_qty = ttk.Entry(root)
entry_qty.place(x=150, y=110, width=200)

# Create buttons for CRUD operations with colors and `place`
add_button = tk.Button(root, text="Add Product", command=add_product, bg="green", fg="white")
add_button.place(x=150, y=150, width=100)

update_button = tk.Button(root, text="Update Product", command=update_product, bg="blue", fg="white")
update_button.place(x=270, y=150, width=100)

delete_button = tk.Button(root, text="Delete Product", command=delete_product, bg="red", fg="white")
delete_button.place(x=150, y=190, width=100)

view_button = tk.Button(root, text="View All Products", command=view_all_products, bg="orange", fg="white")
view_button.place(x=270, y=190, width=100)

# Create a non-editable Text widget for displaying the products
text_display = tk.Text(root, width=50, height=15, state=tk.DISABLED)
text_display.place(x=20, y=230)

root.mainloop()

# Close the database connection when the application is closed
db.close()
