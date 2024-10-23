import tkinter as tk

# Function to start the quiz with the selected difficulty
def start_quiz(difficulty):
    difficulty_window.destroy()  # Close the difficulty selection window
    # This is where you'd start the quiz with the selected difficulty.
    # In this example, we'll just print the selected difficulty.
    print(f"Starting quiz with {difficulty} difficulty.")

# Function to open the difficulty selection window
def open_difficulty_selection():
    global difficulty_window
    difficulty_window = tk.Toplevel()  # Create a new top-level window
    difficulty_window.title("Select Difficulty")  # Set the window title
    difficulty_window.geometry("400x300")  # Set the window size
    difficulty_window.configure(bg="white")  # Set the background color

    # Label for the window title
    title_label = tk.Label(difficulty_window, text="Select Difficulty", font=("Helvetica", 18, "bold"), bg="white")
    title_label.pack(pady=20)  # Add padding around the label

    # Button for "Easy" difficulty
    easy_button = tk.Button(difficulty_window, text="Easy", width=20, height=2, bg="green", command=lambda: start_quiz("easy"))
    easy_button.pack(pady=10)  # Add padding around the button

    # Button for "Challenging" difficulty
    challenging_button = tk.Button(difficulty_window, text="Challenging", width=20, height=2, bg="yellow", command=lambda: start_quiz("challenging"))
    challenging_button.pack(pady=10)  # Add padding around the button

    # Button for "Hard" difficulty
    hard_button = tk.Button(difficulty_window, text="Hard", width=20, height=2, bg="red", command=lambda: start_quiz("hard"))
    hard_button.pack(pady=10)  # Add padding around the button

# Create the main application window
root = tk.Tk()
root.title("Animal Quiz - Difficulty Selection")  # Set the main window title
root.geometry("400x300")  # Set the main window size

# Button to start the quiz, which opens the difficulty selection window
start_button = tk.Button(root, text="Start Quiz", width=20, height=2, command=open_difficulty_selection)
start_button.pack(pady=20)  # Add padding around the button

root.mainloop()  # Start the Tkinter event loop
