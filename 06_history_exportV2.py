import tkinter as tk
from PIL import Image, ImageTk

quiz_results = [
    {"type": "Whose This?", "score": 8},
    {"type": "Who Can Do That?", "score": 7}
]

def export_results():
    with open("quiz_results.txt", "w") as f:
        for result in quiz_results:
            f.write(f"Quiz Type: {result['type']}, Score: {result['score']}\n")
    print("Results exported to quiz_results.txt")

def open_history(main_window):
    main_window.title("Quiz Results History")
    main_window.geometry("800x600")

    # Load the background image
    bg_image = Image.open("images/zebraBG2.png")
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to hold the background image
    bg_label = tk.Label(main_window, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to the image to prevent garbage collection
    bg_label.place(relwidth=1, relheight=1)

    title_label = tk.Label(main_window, text="Quiz Results History", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333333")
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    results_frame = tk.Frame(main_window, bg="#ffffff", bd=2, relief=tk.SUNKEN)
    results_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=700, height=400)

    results_listbox = tk.Listbox(results_frame, font=("Helvetica", 18), bg="#f9f9f9", fg="#333333", selectbackground="#555555", selectforeground="#ffffff")
    results_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for result in quiz_results:
        results_listbox.insert(tk.END, f"Quiz Type: {result['type']}, Score: {result['score']}")

    button_frame = tk.Frame(main_window, bg="#ffffff")
    button_frame.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    export_button = tk.Button(button_frame, text="Export Results", font=("Helvetica", 18), bg="#333333", fg="#ffffff", command=export_results, relief=tk.FLAT)
    export_button.grid(row=0, column=0, padx=10, pady=5)

    close_button = tk.Button(button_frame, text="Close", font=("Helvetica", 18), bg="#333333", fg="#ffffff", command=main_window.quit, relief=tk.FLAT)
    close_button.grid(row=0, column=1, padx=10, pady=5)

root = tk.Tk()
root.title("Animal Quiz - History/Export Page")
root.geometry("800x600")

# Directly open the history page when the application starts
open_history(root)

root.mainloop()
