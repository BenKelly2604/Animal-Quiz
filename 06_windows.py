import tkinter as tk

# Global list to manage open windows
window_stack = []


def close_previous_window():
    """Closes the last opened window."""
    if window_stack:
        # Withdraw (hide) the last window in the stack
        window_stack[-1].withdraw()


def open_new_window(window_title):
    """Opens a new window and closes the previous one."""
    global window_stack
    close_previous_window()

    # Create a new top-level window
    new_window = tk.Toplevel()
    new_window.title(window_title)  # Set the title of the new window
    new_window.geometry("400x300")  # Set the size of the new window
    new_window.configure(bg="white")  # Set the background color of the new window

    # Add a title label to the new window
    title_label = tk.Label(new_window, text=window_title, font=("Helvetica", 18, "bold"), bg="white")
    title_label.pack(pady=20)  # Pack the label with some padding

    # Ensure proper handling when the new window is closed
    new_window.protocol("WM_DELETE_WINDOW", lambda: close_window(new_window))
    window_stack.append(new_window)  # Add the new window to the stack


def close_window(window_to_close=None):
    """Handles the closing of windows and updates the stack."""
    global window_stack
    if window_stack:
        # Pop and destroy the current window
        current_window = window_stack.pop()
        current_window.destroy()
    if window_stack:
        # Deiconify (show) the last window in the stack
        last_window = window_stack[-1]
        last_window.deiconify()


def create_main_window():
    """Creates the main application window."""
    root = tk.Tk()  # Initialize the main window
    root.title("Tab Management Example")  # Set the title of the main window
    root.geometry("400x300")  # Set the size of the main window

    # Create a button to open the first quiz window
    open_tab1_button = tk.Button(root, text="Quiz 1", command=lambda: open_new_window("Information to come..."), font=("Helvetica", 14))
    open_tab1_button.pack(pady=20)  # Pack the button with some padding

    # Create a button to open the second quiz window
    open_tab2_button = tk.Button(root, text="Quiz 2", command=lambda: open_new_window("Information to come..."), font=("Helvetica", 14))
    open_tab2_button.pack(pady=20)  # Pack the button with some padding

    # Create a button to open the learning window
    open_tab3_button = tk.Button(root, text="Learn", command=lambda: open_new_window("Information to come..."), font=("Helvetica", 14))
    open_tab3_button.pack(pady=20)  # Pack the button with some padding

    window_stack.append(root)  # Add the main window to the stack

    root.mainloop()  # Start the main loop of the Tkinter application


def on_main_window_close():
    """Handles the closing of the main application window."""
    global window_stack
    while window_stack:
        # Pop and destroy each window in the stack
        current_window = window_stack.pop()
        current_window.destroy()

if __name__ == "__main__":
    create_main_window()  # Run the function to create the main window
