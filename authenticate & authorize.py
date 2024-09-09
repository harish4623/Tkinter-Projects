import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="auth_system"
)
cursor = conn.cursor()

# Registration Function
def register_user():
    """Registers a new user in the database."""
    user_id, username, password, role = entry_id.get(), entry_username.get(), entry_password.get(), entry_role.get()
    
    if not all([user_id, username, password, role]):
        messagebox.showwarning("Registration Error", "All fields are required!")
    else:
        try:
            cursor.execute("INSERT INTO users (id, username, password, role) VALUES (%s, %s, %s, %s)", (user_id, username, password, role))
            conn.commit()
            messagebox.showinfo("Registration Success", "User registered successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Registration Error", f"Error: {err}")

# Login Function
def login_user(role):
    """Logs in a user based on their role."""
    username, password = entry_username.get(), entry_password.get()
    
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s AND role=%s", (username, password, role))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Success", f"Welcome {username}!\nYour role is {role}.")
        (admin_access if role == 'admin' else user_access)()
    else:
        messagebox.showerror("Login Error", "Invalid username or password!")

# Admin Access and User Access Functions
def open_access_window(title, message):
    """Opens a new access window and closes others."""
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.destroy()
    
    access_window = tk.Toplevel(root)
    access_window.title(title)
    access_window.geometry("300x200")
    access_window.configure(bg="light gray")
    tk.Label(access_window, text=message, font=("Helvetica", 14), bg="light gray").pack(pady=50)

def admin_access():
    open_access_window("Admin Access", "Admin Access Granted!")

def user_access():
    open_access_window("User Access", "User Access Granted!")

# Display Login Form for Selected Role
def display_login(role):
    """Displays login form for the selected role."""
    global entry_username, entry_password

    # Close other windows before opening a new one
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.destroy()
    
    login_window = tk.Toplevel(root)
    login_window.title(f"Login as {role.capitalize()}")
    login_window.geometry("350x250")
    login_window.configure(bg="light blue")

    tk.Label(login_window, text=f"Login as {role.capitalize()}", font=("Helvetica", 16, "bold"), bg="light blue").pack(pady=10)

    frame = ttk.Frame(login_window, padding=20)
    frame.pack(pady=10)

    ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky="W")
    entry_username = ttk.Entry(frame)
    entry_username.grid(row=0, column=1)

    ttk.Label(frame, text="Password:").grid(row=1, column=0, sticky="W")
    entry_password = ttk.Entry(frame, show='*')
    entry_password.grid(row=1, column=1)

    ttk.Button(login_window, text="Login", width=15, command=lambda: login_user(role)).pack(pady=10)

# Display Registration Form
def display_registration():
    """Displays registration form for new users."""
    global entry_id, entry_username, entry_password, entry_role

    # Close other windows before opening a new one
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.destroy()

    reg_window = tk.Toplevel(root)
    reg_window.title("Register New User")
    reg_window.geometry("400x300")
    reg_window.configure(bg="light green")

    tk.Label(reg_window, text="Register New User", font=("Helvetica", 16, "bold"), bg="light green").pack(pady=10)

    frame = ttk.Frame(reg_window, padding=20)
    frame.pack(pady=10)

    ttk.Label(frame, text="User ID:").grid(row=0, column=0, sticky="W")
    entry_id = ttk.Entry(frame)
    entry_id.grid(row=0, column=1)

    ttk.Label(frame, text="Username:").grid(row=1, column=0, sticky="W")
    entry_username = ttk.Entry(frame)
    entry_username.grid(row=1, column=1)

    ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky="W")
    entry_password = ttk.Entry(frame, show='*')
    entry_password.grid(row=2, column=1)

    ttk.Label(frame, text="Role (admin/user):").grid(row=3, column=0, sticky="W")
    entry_role = ttk.Entry(frame)
    entry_role.grid(row=3, column=1)

    ttk.Button(reg_window, text="Register", width=15, command=register_user).pack(pady=10)

# Set up Tkinter window
root = tk.Tk()
root.title("Authentication System")
root.geometry("400x250")
root.configure(bg="lavender")

# Home Page UI Enhancements
tk.Label(root, text="Welcome to the Authentication System", font=("Helvetica", 16, "bold"), bg="lavender").pack(pady=20)

button_frame = ttk.Frame(root, padding=20)
button_frame.pack(pady=20)

# Increased button size with width parameter
ttk.Button(button_frame, text="Login as Admin", width=30, command=lambda: display_login("admin")).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Login as User", width=30, command=lambda: display_login("user")).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Register New User", width=30, command=display_registration).grid(row=2, column=0, padx=10, pady=5)

root.mainloop()

# Close the database connection when the application exits
cursor.close()
conn.close()
