import tkinter as tk
from PIL import Image, ImageTk
import random

# Global variables to store the windows stack and quiz results
window_stack = []
quiz_results = []

# List of animals sorted alphabetically
animal_list = sorted(["Alpaca", "Ant", "Bat", "Bee", "Crocodile", "Deer", "Cheetah", "Duck",
                      "Crab", "Spider", "Rhino", "Cat", "Dog", "Giraffe", "Bear", "Elephant", "Tiger",
                      "Lion", "Zebra", "Kangaroo", "Buffalo", "Beaver", "Donkey", "Tasmanian Devil", "Hamster", "Hawk",
                      "Fox", "Hedgehog", "Horse", "Kiwi", "Lizard", "Leopard", "Koala", "Lemur", "Mole", "Panther",
                      "Pig", "Penguin", "Platypus", "Pelican", "Orangutan", "Polar Bear", "Rabbit", "Sloth", "Seagull",
                      "Red Panda", "Snake", "Sheep", "Squirrel", "Turkey", "Wolf", "Wombat"])

# Dictionary mapping difficulty levels to image path directories
difficulty_path = {
    "easy": "Images/easy/",
}

# Function to close the current window and show the previous one if any
def close_window(window_to_close=None):
    global window_stack
    if window_stack:
        current_window = window_stack.pop()
        current_window.destroy()
    if window_stack:
        last_window = window_stack[-1]
        last_window.deiconify()

# Function to hide the current window without destroying it
def close_previous_window():
    if window_stack:
        window_stack[-1].withdraw()

# Function to validate if the answer is a valid animal name
def validate_answer(answer):
    return answer.strip().lower() in [animal.lower() for animal in animal_list]

# Function to display the next question in the quiz
def display_next_question(quiz_window, idx, score, correct_answers, answer_entry, feedback_label, difficulty, quiz_type):
    answer = answer_entry.get().strip().lower()
    if validate_answer(answer):
        if answer == correct_answers[idx].lower():
            feedback_label.config(text="Correct!", fg="green")
            score += 1
        else:
            feedback_label.config(text=f"Incorrect! The correct answer was {correct_answers[idx]}", fg="red")

        submit_button.config(text="Next Question", command=lambda: load_question(quiz_window, idx + 1, score, correct_answers, difficulty, quiz_type) if idx < len(correct_answers) - 1 else show_results(quiz_window, score, quiz_type))
    else:
        feedback_label.config(text="Please type a valid animal's name", fg="red")

# Function to load a question in the quiz window
def load_question(quiz_window, idx, score, correct_answers, difficulty, quiz_type):
    for widget in quiz_window.winfo_children():
        widget.destroy()

    question_label = tk.Label(quiz_window, text=f"Question {idx + 1}: What is this animal?", font=("Helvetica", 18, "bold"), bg="white")
    question_label.pack(pady=20)

    animal = correct_answers[idx]
    try:
        animal_image = Image.open(f"{difficulty_path[difficulty]}{animal.lower()}.jpg")
        animal_image = resize_image(animal_image, 200, 200)
        animal_photo = ImageTk.PhotoImage(animal_image)

        image_label = tk.Label(quiz_window, image=animal_photo, bg="white")
        image_label.image = animal_photo
        image_label.pack(pady=20)
    except FileNotFoundError:
        image_label = tk.Label(quiz_window, text="Image not available", font=("Helvetica", 18), bg="white")
        image_label.pack(pady=20)

    answer_entry = tk.Entry(quiz_window, font=("Helvetica", 18))
    answer_entry.pack(pady=10)

    feedback_label = tk.Label(quiz_window, text="", font=("Helvetica", 14), bg="white")
    feedback_label.pack(pady=10)

    global submit_button
    submit_button = tk.Button(quiz_window, text="Submit", font=("Helvetica", 18), command=lambda: display_next_question(quiz_window, idx, score, correct_answers, answer_entry, feedback_label, difficulty, quiz_type))
    submit_button.pack(pady=20)

    suggestions_frame = tk.Frame(quiz_window, bg="white")
    suggestions_frame.pack(pady=5)

    suggestions_listbox = tk.Listbox(suggestions_frame, font=("Helvetica", 14), height=5)  # Set height to 5 lines
    suggestions_listbox.pack(fill=tk.BOTH, expand=True)

    answer_entry.bind("<KeyRelease>", lambda event: update_suggestions(event, answer_entry, suggestions_listbox, correct_answers))

# Function to resize an image while maintaining its aspect ratio
def resize_image(image, max_width, max_height):
    w, h = image.size
    ratio = min(max_width / w, max_height / h)
    new_size = (int(w * ratio), int(h * ratio))
    return image.resize(new_size, Image.LANCZOS)

# Function to update the suggestions in the listbox based on user input
def update_suggestions(event, entry, suggestions_listbox, correct_answers):
    suggestions = [animal for animal in animal_list if animal.lower().startswith(entry.get().lower())]
    suggestions_listbox.delete(0, tk.END)
    for suggestion in suggestions:
        suggestions_listbox.insert(tk.END, suggestion)

    def on_select(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        entry.delete(0, tk.END)
        entry.insert(0, value)

    suggestions_listbox.bind('<<ListboxSelect>>', on_select)

# Function to show the results after the quiz is finished
def show_results(quiz_window, score, quiz_type):
    global quiz_results
    quiz_results.append({"type": quiz_type, "score": score})

    for widget in quiz_window.winfo_children():
        widget.destroy()

    result_label = tk.Label(quiz_window, text=f"Your Score: {score}/10", font=("Helvetica", 24, "bold"), bg="white")
    result_label.pack(pady=50)

    close_button = tk.Button(quiz_window, text="Close", command=lambda: close_window(quiz_window), font=("Helvetica", 18))
    close_button.pack(pady=20)

# Function to open the "Whose This?" quiz
def open_whose_this_quiz(difficulty):
    global window_stack
    close_previous_window()

    quiz_window = tk.Toplevel()
    quiz_window.title("Whose This? Quiz")
    quiz_window.geometry("400x600")
    quiz_window.configure(bg="white")

    correct_answers = random.sample(animal_list, 10)
    load_question(quiz_window, 0, 0, correct_answers, difficulty, "Whose This?")

    quiz_window.protocol("WM_DELETE_WINDOW", lambda: close_window(quiz_window))
    window_stack.append(quiz_window)

# Main program entry point
root = tk.Tk()
root.withdraw()  # Hide the root window

open_whose_this_quiz("easy")
root.mainloop()
