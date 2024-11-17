import tkinter as tk

# Global list to manage open windows
window_stack = []


def close_previous_window():
    """Closes the last opened window."""
    if window_stack:
        # Hide the last window in the stack
        last_window = window_stack[-1]
        last_window.withdraw()


def open_new_window(window_title):
    """Opens a new window directly on top of the current active window."""
    global window_stack
    close_previous_window()

    # Get the current geometry of the last active window
    if window_stack:
        current_window = window_stack[-1]
        current_geometry = current_window.geometry()
    else:
        current_geometry = "400x300+100+100"  # Default fallback geometry

    # Create a new top-level window
    new_window = tk.Toplevel()
    new_window.title(window_title)  # Set the title of the new window
    new_window.geometry(current_geometry)  # Place the new window on top of the last active window
    new_window.configure(bg="white")  # Set the background color

    # Add a title label to the new window
    title_label = tk.Label(new_window, text=window_title, font=("Helvetica", 18, "bold"), bg="white")
    title_label.pack(pady=20)

    # Handle window closure
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
        # Show the last window in the stack
        last_window = window_stack[-1]
        last_window.deiconify()


def create_main_window():
    """Creates the main application window."""
    root = tk.Tk()  # Initialize the main window
    root.title("Tab Management Example")  # Set the title of the main window
    root.geometry("400x300+200+200")  # Set the size and position of the main window

    # Create buttons to open new tabs
    button1 = tk.Button(root, text="Open Quiz 1", command=lambda: open_new_window("Quiz 1"), font=("Helvetica", 14))
    button1.pack(pady=20)

    button2 = tk.Button(root, text="Open Quiz 2", command=lambda: open_new_window("Quiz 2"), font=("Helvetica", 14))
    button2.pack(pady=20)

    button3 = tk.Button(root, text="Open Learn", command=lambda: open_new_window("Learn"), font=("Helvetica", 14))
    button3.pack(pady=20)

    window_stack.append(root)  # Add the main window to the stack

    root.protocol("WM_DELETE_WINDOW", on_main_window_close)
    root.mainloop()


def on_main_window_close():
    """Handles the closing of the main application window."""
    global window_stack
    while window_stack:
        # Pop and destroy each window in the stack
        current_window = window_stack.pop()
        current_window.destroy()


if __name__ == "__main__":
    create_main_window()
