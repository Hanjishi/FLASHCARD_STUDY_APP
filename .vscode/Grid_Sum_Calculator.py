import tkinter as tk

def compute_sum():
    try:

        num1 = float(entry1.get())
        num2 = float(entry2.get())

        result = num1 + num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


root = tk.Tk()
root.title("Sum Calculator")


root.geometry("375x150")

label1 = tk.Label(root, text="Enter First Number:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter Second Number:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

compute_button = tk.Button(root, text="Compute Sum", command=compute_sum)
compute_button.grid(row=3, column=1)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=1)

root.mainloop()