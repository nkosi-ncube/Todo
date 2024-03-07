import questionary


def ask_questions():
    # Text Question
    name = questionary.text("What is your name?").ask()

    # Password Question
    password = questionary.password("Enter your password").ask()

    # Confirm Question
    confirmation = questionary.confirm("Are you sure?").ask()

    # Select Question
    selected_option = questionary.select("Choose an option:", choices=[
                                         "Option A", "Option B", "Option C"]).ask()

    # Rawselect Question
    raw_selected_option = questionary.rawselect(
        "Choose an option:", choices=["Option X", "Option Y", "Option Z"]).ask()

    # Path Question
    file_path = questionary.path("Enter file path:").ask()

    # Auto Ask Question
    auto_selected_option = questionary.autocomplete(
        "Choose an option:", choices=["Apple", "Banana", "Cherry"]).ask()

    # Editor Question
    notes = questionary.text(
        "Write your notes:", validate=lambda text: True).ask()

    # Display the collected answers
    print("\nCollected Answers:")
    print(f"Name: {name}")
    print(f"Password: {password}")
    print(f"Confirmation: {confirmation}")
    print(f"Selected Option: {selected_option}")

    print(f"Raw Selected Option: {raw_selected_option}")
    print(f"File Path: {file_path}")
    print(f"Auto Selected Option: {auto_selected_option}")
    print(f"Notes:\n{notes}")


if __name__ == "__main__":
    ask_questions()
