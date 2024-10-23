import tkinter as tk
from PIL import Image, ImageTk
import random
import textwrap

# Sorted list of animal names
animal_list = sorted(["Alpaca", "Ant", "Bat", "Bee", "Crocodile", "Deer", "Cheetah", "Duck",
                      "Crab", "Spider", "Rhino", "Cat", "Dog", "Giraffe", "Bear", "Elephant", "Tiger",
                      "Lion", "Zebra", "Kangaroo", "Buffalo", "Beaver", "Donkey", "Tasmanian Devil", "Hamster", "Hawk",
                      "Fox", "Hedgehog", "Horse", "Kiwi", "Lizard", "Leopard", "Koala", "Lemur", "Mole", "Panther",
                      "Pig", "Penguin", "Platypus", "Pelican", "Orangutan", "Polar Bear", "Rabbit", "Sloth", "Seagull",
                      "Red Panda", "Snake", "Sheep", "Squirrel", "Turkey", "Wolf", "Wombat"])

# Descriptions of animals
animal_descriptions = {
    "bear": "Which are large, heavy mammals with shaggy hair.",
    "cat": "Which are small, carnivorous mammals.",
    "dog": "Which are domesticated mammals, not natural wild animals.",
    "sheep": "Which are domesticated ruminant mammals typically kept as livestock.",
    "alpaca": "Which are domesticated camelids known for their wool.",
    "ant": "Which are small insects known for their complex colonies.",
    "bat": "Which are mammals capable of sustained flight.",
    "bee": "Which are insects known for their role in pollination.",
    "crocodile": "Which are large aquatic reptiles with powerful jaws.",
    "deer": "Which are hoofed mammals known for their antlers.",
    "cheetah": "Which are large cats known for their incredible speed.",
    "duck": "Which are waterfowl known for their quacking.",
    "crab": "Which are crustaceans with a hard exoskeleton.",
    "spider": "Which are arachnids known for their web-spinning abilities.",
    "rhino": "Which are large herbivorous mammals known for their horns.",
    "giraffe": "Which are the tallest land animals, known for their long necks.",
    "elephant": "Which are the largest land animals, known for their trunks.",
    "tiger": "Which are large predatory cats with distinctive stripes.",
    "lion": "Which are large cats known as the kings of the jungle.",
    "zebra": "Which are equids known for their black and white stripes.",
    "kangaroo": "Which are marsupials known for their hopping.",
    "buffalo": "Which are large bovines known for their strength.",
    "beaver": "Which are rodents known for building dams.",
    "donkey": "Which are domesticated equids known for their endurance.",
    "tasmanian devil": "Which are carnivorous marsupials known for their strong jaws.",
    "hamster": "Which are small rodents often kept as pets.",
    "hawk": "Which are birds of prey known for their keen eyesight.",
    "fox": "Which are small to medium-sized omnivorous mammals.",
    "hedgehog": "Which are small mammals known for their spiny backs.",
    "horse": "Which are large domesticated mammals known for their speed and strength.",
    "kiwi": "Which are flightless birds native to New Zealand.",
    "lizard": "Which are reptiles with scaly skin and elongated bodies.",
    "leopard": "Which are large cats known for their spotted coats.",
    "koala": "Which are arboreal marsupials native to Australia.",
    "lemur": "Which are primates native to Madagascar.",
    "mole": "Which are small burrowing mammals with velvety fur.",
    "panther": "Which are large cats, often black-coated leopards or jaguars.",
    "pig": "Which are domesticated omnivorous mammals.",
    "penguin": "Which are flightless birds adapted to life in the water.",
    "platypus": "Which are egg-laying mammals with duck bills.",
    "pelican": "Which are large water birds with distinctive pouches.",
    "orangutan": "Which are large primates known for their reddish fur.",
    "polar bear": "Which are large carnivorous bears native to the Arctic.",
    "rabbit": "Which are small mammals with long ears.",
    "sloth": "Which are slow-moving arboreal mammals.",
    "seagull": "Which are seabirds known for their adaptability.",
    "red panda": "Which are small mammals with reddish-brown fur.",
    "snake": "Which are legless reptiles.",
    "squirrel": "Which are small rodents known for their bushy tails.",
    "turkey": "Which are large birds native to North America.",
    "wolf": "Which are large wild canines known for their pack behavior.",
    "wombat": "Which are burrowing marsupials native to Australia."
}

# Function to wrap text within a specified width
def wrap_text(text, width):
    return "\n".join(textwrap.fill(line, width) for line in text.split("\n"))

# Function to load multiple-choice question in the quiz window
def load_mc_question(quiz_window, idx, score, questions, correct_answers):
    # Clear all widgets in the quiz window
    for widget in quiz_window.winfo_children():
        widget.destroy()

    # Display the question
    question_label = tk.Label(quiz_window, text=f"Question {idx + 1}: {questions[idx]['question']}",
                              font=("Helvetica", 14, "bold"), bg="white", wraplength=550, justify=tk.LEFT)
    question_label.pack(pady=10)

    # Entry field for the answer
    answer_entry = tk.Entry(quiz_window, font=("Helvetica", 14), width=40)
    answer_entry.pack(pady=5)

    # Frame to hold multiple-choice options
    options_frame = tk.Frame(quiz_window, bg="white")
    options_frame.pack(pady=10)

    # Display the options
    options = questions[idx]['options']
    for i, option in enumerate(options):
        option_label = tk.Label(options_frame, text=f"{chr(65 + i)}. {option}", font=("Helvetica", 14), width=20,
                                height=2, bg="lightgray", relief="groove")
        option_label.grid(row=i // 2, column=i % 2, padx=5, pady=5)

    # Label to display feedback
    feedback_label = tk.Label(quiz_window, text="", font=("Helvetica", 12), bg="white")
    feedback_label.pack(pady=5)

    # Button to submit the answer
    submit_button = tk.Button(quiz_window, text="Submit", font=("Helvetica", 14),
                              command=lambda: display_next_mc_question(quiz_window, idx, score, questions,
                                                                       correct_answers, answer_entry, feedback_label,
                                                                       submit_button))
    submit_button.pack(pady=10)

# Function to handle option selection
def select_option(option, answer_entry):
    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, option)

# Function to display the next multiple-choice question
def display_next_mc_question(quiz_window, idx, score, questions, correct_answers, answer_entry, feedback_label,
                             submit_button):
    answer = answer_entry.get().strip().capitalize()
    correct_option = correct_answers[idx]
    option_letters = ['A', 'B', 'C', 'D']
    options = questions[idx]['options']
    valid_options = option_letters + [opt.capitalize() for opt in options]

    # Check if the answer is valid
    if answer in valid_options:
        if answer == correct_option or (
                answer in option_letters and options[option_letters.index(answer)] == correct_option):
            feedback_label.config(text="Correct!", fg="green")
            score += 1
        else:
            feedback_label.config(text=f"Incorrect! The correct answer was {correct_option}", fg="red")

        # Update the button to load the next question or show results
        submit_button.config(text="Next Question",
                             command=lambda: load_mc_question(quiz_window, idx + 1, score, questions,
                                                              correct_answers) if idx < len(
                                 correct_answers) - 1 else show_results(quiz_window, score))
    else:
        feedback_label.config(text="Please enter a valid option (A, B, C, D) or animal name.", fg="red")

# Function to display the final results
def show_results(quiz_window, score):
    for widget in quiz_window.winfo_children():
        widget.destroy()

    result_label = tk.Label(quiz_window, text=f"Your Score: {score}/10", font=("Helvetica", 18, "bold"), bg="white")
    result_label.pack(pady=20)

    close_button = tk.Button(quiz_window, text="Close", command=quiz_window.destroy, font=("Helvetica", 14))
    close_button.pack(pady=10)

# Function to open the quiz window
def open_who_can_do_that_quiz():
    quiz_window = tk.Toplevel()
    quiz_window.title("Who Can Do That? Quiz")
    quiz_window.geometry("600x400")
    quiz_window.configure(bg="white")

    questions = []
    correct_answers = []

    # Generate 10 random questions
    for _ in range(10):
        animal = random.choice(list(animal_descriptions.keys()))
        correct_answers.append(animal.capitalize())
        options = list(set(random.sample(animal_list, 3) + [animal.capitalize()]))  # Ensure unique options
        random.shuffle(options)
        questions.append({"question": animal_descriptions[animal], "options": options})

    load_mc_question(quiz_window, 0, 0, questions, correct_answers)

# Main function to start the application
root = tk.Tk()
root.withdraw()  # Hide the root window

open_who_can_do_that_quiz()
root.mainloop()
