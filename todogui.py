import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Tk, Text, END, IntVar, simpledialog
import tkinter.messagebox as messagebox
from tkcalendar import DateEntry
import csv

def authenticate_user():
    while True:
        choice = simpledialog.askstring("Authentication", "Do you want to login or sign up? (login/signup)")
        if choice.lower() == "login":
            username = simpledialog.askstring("Login", "Enter your username:")
            password = simpledialog.askstring("Login", "Enter your password:")
            if login(username, password):
                return True
            else:
                messagebox.showerror("Authentication Failed", "Invalid username or password. Please try again.")
        elif choice.lower() == "signup":
            username = simpledialog.askstring("Signup", "Enter a new username:")
            password1 = simpledialog.askstring("Signup", "Enter a password:")
            password2 = simpledialog.askstring("Signup", "Confirm your password:")
            if signup(username, password1, password2):
                messagebox.showinfo("Signup Successful", "Account created successfully!")
                return True
            else:
                messagebox.showerror("Signup Failed", "Passwords do not match. Please try again.")
        else:
            messagebox.showerror("Invalid Choice", "Please enter 'login' or 'signup'.")

def view_todo_list():
    try:
        with open('todolist.txt', 'r') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        return ['Todo list is empty.']
    
    
def update_todo_list(text_widget, check_vars):
    text_widget.delete(1.0, END)  # Clear existing content
    content = view_todo_list()

    # Ensure that check_vars has enough elements for each line in the content
    while len(check_vars) < len(content):
        check_vars.append(IntVar())

    for i, line in enumerate(content, start=1):
        check_var = check_vars[i - 1]
        text_widget.window_create(END, window=ttk.Checkbutton(text_widget, variable=check_var))
        text_widget.insert(END, f" {i}. {line}")


def add_to_list(date, event):
    with open('todolist.txt', 'a') as file:
        # Check if the date already contains "0:" and remove it if present
        date = date.replace("0:", "")

        file.write(f"{date}: {event}\n")
    messagebox.showinfo("Success", "Event added to the list successfully!")


def remove_from_list(line_number, check_vars, text_widget):
    try:
        with open('todolist.txt', 'r') as file:
            lines = file.readlines()
        with open('todolist.txt', 'w') as file:
            for i, line in enumerate(lines, start=1):
                if i != line_number:
                    file.write(line)

        # Update the Text widget and checkboxes after removing an item
        update_todo_list(text_widget, check_vars)

    except FileNotFoundError:
        print("Todo list is empty.")
import csv

def login(username, password):
    with open("users.csv", newline='') as user_details:
        reader = csv.reader(user_details)
        for row in reader:
            if len(row) == 4 and row[0] == username and row[2] == password:
                return True
    return False

def signup(username, password1, password2):
    if password1 == password2:
        with open("users.csv", mode='a', newline='') as user_details:
            writer = csv.writer(user_details)
            writer.writerow([username, '', password1])  # You might want to include other user details
        return True
    return False


def gui_creator():
    # Authenticate user before opening the TODO app
    if not authenticate_user():
        return

    root = ttk.Window(themename="superhero")
    root.title("TODO APP")
    root.geometry("800x600")

    # Text widget to display the to-do list
    todo_text = Text(root, height=20, width=100)
    todo_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    # Add a list to hold IntVar for each checkbox
    check_vars = []

    def view_button_clicked():
        update_todo_list(todo_text, check_vars)

    b4 = ttk.Button(root, text='View to-do list', bootstyle=INFO, command=view_button_clicked)
    b4.grid(row=3, column=1, padx=5, pady=5)

    l1 = ttk.Label(root, text="Select the day of event:", bootstyle="primary")
    l1.grid(row=0, column=0, padx=5, pady=5, columnspan=1)

    cal = ttk.DateEntry(root, bootstyle="primary")
    cal.grid(row=0, column=2, padx=5, pady=5)

    l2 = ttk.Label(root, text="Enter the event title:", bootstyle="primary")
    l2.grid(row=1, column=0, padx=5, pady=5, columnspan=1)

    info_entry = ttk.Entry(root, bootstyle="info", width=25)
    info_entry.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

    b3 = ttk.Button(root, text='Add to List', bootstyle=SUCCESS,
                    command=lambda: add_to_list(cal.entry.get(), info_entry.get()))
    b3.grid(row=3, column=0, padx=5, pady=5)

    b6 = ttk.Button(root, text='Remove from list', bootstyle=DANGER,
                    command=lambda: remove_from_list(1, check_vars, todo_text,))
    b6.grid(row=3, column=2, padx=5, pady=5)

    # Initialize IntVar for each line in the to-do list
    content = view_todo_list()
    for _ in range(len(content)):
        check_vars.append(IntVar())

    root.mainloop()

if __name__ == '__main__':
    gui_creator()
