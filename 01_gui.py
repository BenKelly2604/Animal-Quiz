import tkinter as tk
from PIL import Image, ImageTk

# Function to handle closing the main window
def on_main_window_close():
    root.quit()

# Function to open the help window
def open_help():
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("350x405")
    help_window.configure(bg="white")

    # Load and resize help image
    help_image = Image.open("Images/help_guy.png")
    help_image = help_image.resize((200, 200))
    help_photo = ImageTk.PhotoImage(help_image)

    # Display help image
    help_image_label = tk.Label(help_window, image=help_photo, bg="white")
    help_image_label.pack()
    help_image_label.image = help_photo  # Keep a reference to avoid garbage collection

    # Help text
    help_text = """
    Welcome to Animal Quiz!

    This application helps you learn about various animals
    in a fun and interactive way.

    To get started, you can click on the "Learn" button
    to explore information about each animal.

    If you want to test your knowledge, click on the "Quiz"
    button to take a quiz about the animals.

    Enjoy learning!
    """
    # Display help text
    help_label = tk.Label(help_window, text=help_text, justify=tk.LEFT, bg="white")
    help_label.pack(padx=20, pady=10)

    # Close button for the help window
    close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)

# Initialize the main window
root = tk.Tk()
root.title("Animal Quiz")
root.geometry("800x600")

# Load and set the background image
background_image = Image.open("Images/GUIFinal.png")
background_image = background_image.resize((800, 500))
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)
background_label.lower()  # Ensure the background is behind all other widgets

# Title label
title_label = tk.Label(root, text="Whose that? - Animal Quiz", font=("Helvetica", 35, "bold"), fg="black", bg=None)
title_label.place(relx=0.1, rely=0.05, anchor=tk.W)

# Welcome text box
welcome_text = "Welcome to the animal learning and quiz program! If you're confused feel free to click the help button! But other than that explore the program and have fun!"
welcome_label = tk.Label(root, text=welcome_text, font=("Helvetica", 11), wraplength=200, justify=tk.CENTER, bg="white", fg="black")
welcome_label.place(relx=0.325, rely=0.475, anchor=tk.CENTER)

# Load and resize the banana image for buttons
banana_image = Image.open("Images/banana.png")
banana_image = banana_image.resize((125, 80))
banana_photo = ImageTk.PhotoImage(banana_image)

# Learn button
learn_button = tk.Button(root, text="Learn", width=125, height=75, fg="black", image=banana_photo, compound="center", borderwidth=0)
learn_button['font'] = ('Arial', 20, 'bold')
learn_button.place(relx=0.3, rely=0.925, anchor=tk.CENTER)

# Quiz button
quiz_button = tk.Button(root, text="Quiz", width=125, height=75, fg="black", image=banana_photo, compound="center", borderwidth=0)
quiz_button['font'] = ('Arial', 20, 'bold')
quiz_button.place(relx=0.5, rely=0.925, anchor=tk.CENTER)

# History button (currently disabled)
history_button = tk.Button(root, text="History", width=125, height=75, fg="black", image=banana_photo, compound="center", borderwidth=0, state=tk.DISABLED)
history_button['font'] = ('Arial', 20, 'bold')
history_button.place(relx=0.7, rely=0.925, anchor=tk.CENTER)

# Help button
help_button = tk.Button(root, text="Help/info", width=10, height=2, bg=None, fg="black", command=open_help, borderwidth=0)
help_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

# Protocol to handle window close event
root.protocol("WM_DELETE_WINDOW", on_main_window_close)

# Start the main event loop
root.mainloop()
