import csv
import questionary
from termcolor import colored
import sys

def start_screen():
    print(colored("______________________________ ", color="green", attrs=["bold"]))
    print(colored("Welcome to the ToDoApp ", color="green", attrs=["bold"]))
    print(colored("______________________________ ", color="green", attrs=["bold"]))
    print(colored("These are the available commands to run the system:", attrs=["bold"]))
    print("1. view_to_do_list\n2. off\n3. add_to_list\n4. remove_from_list")

def shutdown():
    print(colored("System shutting down. Goodbye ...", color="red", attrs=["bold"]))
    sys.exit()

def read_csv(csvfile):
    csv_contents = []
    with open(csvfile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_contents.append(row)
    return csv_contents

def write_to_csv(filename, details):
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow(details)

def view_to_do_list(filename):
    with open(filename) as todofile:
        contents = todofile.readlines()
        for index, row in enumerate(contents):
            print(index + 1, row)

def remove_from_list(filename, position):
    events = []
    with open(filename) as todofile:
        contents = todofile.readlines()
        for row in contents:
            events.append(row)
    events.pop(position - 1)
    with open(filename, "w") as f:
        f.writelines(events)
    print(colored("Successfully removed event.", color="red", attrs=["bold"]))

def add_to_list(filename, event):
    with open(filename, "a") as todofile:
        todofile.write("\n" + event + " Not Done\n")
    print(colored("Successfully added new event.", color="green", attrs=["bold"]))

def access_system():
    on = True
    print("Access to the system has been granted")
    start_screen()
    while on:
        command = input(colored("Enter a command:", color="green", attrs=["bold"]))
        if command == "view_to_do_list":
            view_to_do_list("todolist.txt")
        elif command == "off":
            shutdown()
        elif command == "add_to_list":
            descr = input("Write a description for the event:")
            add_to_list("todolist.txt", descr)
        elif command == "remove_from_list":
            view_to_do_list("todolist.txt")
            position = int(input("Enter the position of the event to be removed:"))
            remove_from_list("todolist.txt", position)
        else:
            print(colored("Please enter a valid command", color="red", attrs=["bold"]))

def run_system():
    file = "login.csv"
    choice = questionary.select(
        "Choose sign up if it's the first time or login if you already have an account:",
        choices=["login", "signup"]).ask()
    if choice == "signup":
        signup(file)
        login(file)
        access_system()
    else:
        login(file)
        access_system()

def signup(file):
    correct_details = False
    while not correct_details:
        username = questionary.text("Enter username:").ask()
        fullnames = questionary.text("Enter fullname:").ask()
        password1 = questionary.password("Enter your password:").ask()
        password2 = questionary.password("Confirm your password:").ask()
        available_users = read_csv(file)

        if not available_users or all(username != user.get("username") for user in available_users):
            if password1 == password2:
                write_to_csv(file, details=[username, fullnames, password1, password2])
                print(colored("User successfully signed up. Please log in.", color="green", attrs=["bold"]))
                correct_details = True
            else:
                print(colored("Passwords did not match", color="red", attrs=["blink"]))
        else:
            print("Username already exists.")

def login(file):
    available_users = read_csv(file)
    credentials_correct = False

    while not credentials_correct:
        username = questionary.text("Enter username:").ask()
        password1 = questionary.password("Enter your password:").ask()
        my_list = list(map(lambda x: x.get("username") == username, available_users))

        if any(my_list):
            index = my_list.index(True)
            current_user = available_users[index]

            if current_user.get("password1") == password1:
                print(colored("Login successful", color="green", attrs=["bold"]))
                credentials_correct = True
            else:
                print("Incorrect credentials")
        else:
            print("You are not in our database. Restart the app and sign up")

if __name__ == "__main__":
    run_system()
