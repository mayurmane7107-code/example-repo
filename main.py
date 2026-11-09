import tkinter as tk

root = tk.Tk()

root.title("welcome window")
root.geometry("700x400")

welcome_font = ("Helvetica", 30, "bold")
welcome_label = tk.Label(root, text="Welcome to my first github project!", font=welcome_font)
welcome_label.pack(expand=True, pady=40)

root.mainloop()