import tkinter as tk


def get_window_geometry(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = window.winfo_x()
    y = window.winfo_y()
    return (x, y, width, height)


def open_tab(title, size):
    root.withdraw()  # Hide the main window
    x, y, width, height = get_window_geometry(root)

    tab_width, tab_height = map(int, size.split('x'))
    new_x = x + (width - tab_width) // 2
    new_y = y + (height - tab_height) // 2

    tab = tk.Toplevel()
    tab.title(title)
    tab.geometry(f"{size}+{new_x}+{new_y}")

    tab_label = tk.Label(tab, text=f"This is {title}", font=("Helvetica", 18), bg="white")
    tab_label.pack(pady=20)

    def on_close():
        tab.destroy()
        root.deiconify()  # Show the main window

    tab.protocol("WM_DELETE_WINDOW", on_close)


# Functions for each tab
def open_tab1():
    open_tab("Tab 1", "400x300")


def open_tab2():
    open_tab("Tab 2", "500x400")


def open_tab3():
    open_tab("Tab 3", "600x500")


def open_tab4():
    open_tab("Tab 4", "700x600")


def open_tab5():
    open_tab("Tab 5", "800x700")


# Main program entry point
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("800x600")
    root.configure(bg="white")

    # Create buttons for each tab
    button1 = tk.Button(root, text="Open Tab 1", font=("Helvetica", 18), command=open_tab1)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Open Tab 2", font=("Helvetica", 18), command=open_tab2)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Open Tab 3", font=("Helvetica", 18), command=open_tab3)
    button3.pack(pady=10)

    button4 = tk.Button(root, text="Open Tab 4", font=("Helvetica", 18), command=open_tab4)
    button4.pack(pady=10)

    button5 = tk.Button(root, text="Open Tab 5", font=("Helvetica", 18), command=open_tab5)
    button5.pack(pady=10)

    root.mainloop()
