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


root.geometry("300x260")

label1 = tk.Label(root, text="Enter First Number:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Second Number:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

compute_button = tk.Button(root, text="Compute Sum", command=compute_sum)
compute_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()