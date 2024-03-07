import questionary

questions = [
    {
        "type": "checkbox",
        "name": "question1",
        "message": "Select options for Question 1:",
        "choices": ["Option 1", "Option 2", "Option 3"],
    },
    {
        "type": "checkbox",
        "name": "question2",
        "message": "Select options for Question 2:",
        "choices": ["Option A", "Option B", "Option C"],
    },
    # Add more questions as needed
]

answers = questionary.prompt(questions)

print("Selected options:")
for question, selected_options in answers.items():
    print(f"{question}: {', '.join(selected_options)}")

import questionary

questions = [
    {
        "type": "text",
        "name": "name",
        "message": "What is your name?",
    },
    {
        "type": "confirm",
        "name": "confirmed",
        "message": "Are you confirmed?",
    },
    {
        "type": "select",
        "name": "color",
        "message": "Pick a color:",
        "choices": ["red", "green", "blue"],
    },
]

answers = questionary.prompt(questions)

print("Answers:")
print(answers)
 

 