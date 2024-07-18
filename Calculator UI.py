import tkinter as tk

# Create main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Create screen to display the calculation
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Define the button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Define button layout
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', ' '
]

# Create buttons and add them to the frame
row = 0
col = 0
for button in buttons:
    if button != ' ':
        btn = tk.Button(button_frame, text=button, font="lucida 15 bold", height=2, width=4)
        btn.grid(row=row, column=col, padx=5, pady=5)
        btn.bind("<Button-1>", lambda event, btn=button: screen.set(
            str(eval(screen.get())) if btn == '=' else "" if btn == 'C' else screen.get() + btn
        ))
    col += 1
    if col > 4:
        col = 0
        row += 1

# Run the application
root.mainloop()
