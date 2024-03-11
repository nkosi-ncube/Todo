import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Tk, LEFT, Text, END, simpledialog
import tkinter.messagebox as messagebox
from tkcalendar import DateEntry



root = ttk.Window(themename="superhero")
def view_todo_list():
    try:
        with open('todolist.txt', 'r') as file:
            content = file.readlines()
            return content
    except FileNotFoundError:
        return ['Todo list is empty.']

def update_todo_list(text_widget):
    text_widget.delete(1.0, END)  # Clear existing content
    content = view_todo_list()
    for i, line in enumerate(content, start=1):
        text_widget.insert(END, f"{i}. {line}")

def add_to_list(date, event):
    with open('todolist.txt', 'a') as file:
        file.write(f"{date}: {event}\n")
    messagebox.showinfo("Success", "Event added to the list successfully!")

def remove_from_list(line_number):
    try:
        with open('todolist.txt', 'r') as file:
            lines = file.readlines()
        with open('todolist.txt', 'w') as file:
            for i, line in enumerate(lines, start=1):
                if i != line_number:
                    file.write(line)
    except FileNotFoundError:
        print("Todo list is empty.")


def gui_creator():
    
    root.title("TODO APP")
    root.geometry("800x600")

    # Label
    l1 = ttk.Label(root, text="Select the day of event:", bootstyle="primary")
    l1.grid(row=0, column=0, padx=5, pady=5,columnspan=1)

    l1 = ttk.Label(root, text="Enter the event title:", bootstyle="primary")
    l1.grid(row=1, column=0, padx=5, pady=5,columnspan=1)

   

    # Entry
    info_entry = ttk.Entry(root, bootstyle="info",width=25)
    info_entry.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

    # Buttons
    b3 = ttk.Button(root, text='Add to List', bootstyle=SUCCESS,
                    command=lambda: add_to_list(cal.entry.get(), info_entry.get()))
    b3.grid(row=3, column=0, padx=5, pady=5)

    # Text widget to display the to-do list
    todo_text = Text(root, height=20, width=100)
    todo_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
    cal = ttk.DateEntry(root, bootstyle="primary")
    cal.grid(row=0, column=2, padx=5, pady=5)
    def view_button_clicked():
        update_todo_list(todo_text)

    b4 = ttk.Button(root, text='View to-do list', bootstyle=INFO, command=view_button_clicked)
    b4.grid(row=3, column=1, padx=5, pady=5)

    def remove_button_clicked():
        line_number = simpledialog.askinteger("Remove from List", "Enter line number to delete:")
        if line_number:
            remove_from_list(line_number)
            update_todo_list(todo_text)

    b6 = ttk.Button(root, text='Remove from list', bootstyle=DANGER, command=remove_button_clicked)
    b6.grid(row=3, column=2, padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    gui_creator()
