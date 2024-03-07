import csv
import questionary
from termcolor import colored
import sys
import getpass


def keep_track_of_login_state(feedback):
    state = {"username": "", "logged_in": feedback}
    return state


def start_screen():
    print(colored("______________________________ ", color="green", attrs=["bold"]))
    print()
    print(colored("Welcome to the ToDoApp ", color="green", attrs=["bold"]))
    print(colored("______________________________ ", color="green", attrs=["bold"]))
    print()
    print(colored(
        "These are the avaialble commands to run system\n1.view_to_do_list\n2.off\n3.add_to_list\n4.remove_from_list", attrs=["bold"]))


def shutdown():
    print(colored("System shutting down.Goodbye ...",
          color="red", attrs=["bold"]))
    sys.exit()


def login(file):

    available_users = read_csv(file)
    credentials_correct = False
   
    while not credentials_correct:
        username = questionary.text("Enter username:").ask()
        password1 = questionary.password("Enter your password:").ask()
        mylist = list(map(lambda x: x.get("username")
                      == username, available_users))
      
        index = mylist.index(True)
        if any(mylist):

            current_user = available_users[index]

            if current_user.get("password1") == password1:
                print(colored("Login succesful",
                      color="green", attrs=["bold"]))
             
                credentials_correct = True
            else:
                print("incorrect credentials")
        else:
            print("You are not in our database.Restart app and sign up")


def signup(file):
    correct_details = False
    while not correct_details:
        username = questionary.text("Enter username:").ask()
        fullnames = questionary.text("Enter fullname:").ask()
        password1 = questionary.password("Enter your password:").ask()
        password2 = questionary.password("Confirm your password:").ask()
        available_users = read_csv(file)
        if len(available_users) > 0:
            if all(username != user.get("username") for user in available_users):
                if password1 == password2:
                    write_to_csv(file, details=[
                        username, fullnames, password1, password2])
                    print(colored("users succesfully signed up.Please login in",
                                  color="green", attrs=["bold"]))
                    correct_details = True
                else:
                    print(colored("Passwords did not match",
                          color="red", attrs=["blink"]))

            else:
                print("Username already exists.")

        else:
            if password1 == password2:
                write_to_csv(file, details=[
                    username, fullnames, password1, password2])
                print(colored("users succesfully signed up",
                              color="green", attrs=["bold"]))
                correct_details = True


def read_csv(csvfile):
    csv_contens = []
    with open(csvfile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_contens.append(row)
    return csv_contens


def write_to_csv(filename, details):
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow(details)


def view_to_do_list(filename):
    with open(filename) as todofile:
        contents = todofile.readlines()
        for index, row in enumerate(contents):
            print(index+1, row)


def remove_from_list(filename,position):
    events=[]
    with open(filename) as todofile:
        contents = todofile.readlines()
        for index, row in enumerate(contents):
           
            events.append(row)
    events.remove(events[position-1])
    with open(filename,"w") as f:
        for event in events:        
            f.write(event)
    print(colored("Succesfully removed event.",color="red",attrs=["bold"]))
   
    

    


def add_to_list(filename,event):
    with open(filename,"a") as todofile:
        todofile.write("\n"+event)
    print(colored("Succesfully added new event.",color="green",attrs=["bold"]))
       


def access_system():
    on = True
    print("Access to system has been granted")
    start_screen()
    while on:
        command = input(colored("Enter a command:",
                        color="green", attrs=["bold"]))
        if command == "view_to_do_list":
            view_to_do_list("todolist.txt")
        elif command == "off":
            shutdown()
        elif command=="add_to_list":
            descr = input("W,ite a description for the event:")
            add_to_list("todolist.txt",descr)

        elif command=="remove_from_list":
            view_to_do_list("todolist.txt")
            
            position =int(input("Enter the position of event to be removed:"))
            remove_from_list("todolist.txt",position)

        else:
            print(colored("Please enter a valid command",
                  color="red", attrs=["bold"]))


def run_system():
    file = "login.csv"
    choice = questionary.select(
        "Choose sign up if its first time or login if you already have an account:", choices=["login", "signup"]).ask()
    if choice == "signup":
        signup(file)
        login(file)
        access_system()

    else:
        login(file)
        access_system()


if __name__ == "__main__":
    run_system()
