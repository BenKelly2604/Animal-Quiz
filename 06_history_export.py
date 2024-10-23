import tkinter as tk

quiz_results = [
    {"type": "Whose This?", "score": 8},
    {"type": "Who Can Do That?", "score": 7}
]

def export_results():
    with open("quiz_results.txt", "w") as f:
        for result in quiz_results:
            f.write(f"Quiz Type: {result['type']}, Score: {result['score']}\n")
    print("Results exported to quiz_results.txt")

def open_history():
    history_window = tk.Toplevel()
    history_window.title("Quiz Results History")
    history_window.geometry("800x600")
    history_window.configure(bg="white")

    title_label = tk.Label(history_window, text="Quiz Results History", font=("Helvetica", 24, "bold"), bg="white")
    title_label.pack(pady=20)

    results_frame = tk.Frame(history_window, bg="white")
    results_frame.pack(fill=tk.BOTH, expand=True)

    results_listbox = tk.Listbox(results_frame, font=("Helvetica", 18))
    results_listbox.pack(fill=tk.BOTH, expand=True)

    for result in quiz_results:
        results_listbox.insert(tk.END, f"Quiz Type: {result['type']}, Score: {result['score']}")

    export_button = tk.Button(history_window, text="Export Results", font=("Helvetica", 18), command=export_results)
    export_button.pack(pady=20)

    close_button = tk.Button(history_window, text="Close", font=("Helvetica", 18), command=history_window.destroy)
    close_button.pack(pady=10)

root = tk.Tk()
root.title("Animal Quiz - History/Export Page")
root.geometry("800x600")

open_history_button = tk.Button(root, text="Open History", width=20, height=2, command=open_history)
open_history_button.pack(pady=20)

root.mainloop()
