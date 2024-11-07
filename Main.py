import tkinter as tk
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
import os


def upload_and_convert():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        try:
            
            # Read CSV
            df = pd.read_csv(filepath)
            
            # Store the converted DataFrame temporarily
            global converted_df
            converted_df = df
            
            messagebox.showinfo("Success", "Excel file change completed")
            save_button.config(state=tk.NORMAL)  # Enable save button
            
        except Exception as e:

            messagebox.showerror("Error", f"Error converting file: {e}")


def save_excel():
    # Get the desktop directory
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    # File path to save the Excel file
    filepath = os.path.join(desktop, "output.xlsx")
    
    try:
        # Save the DataFrame to the specified file
        converted_df.to_excel(filepath, index=False)
        messagebox.showinfo("Success", f"Excel file saved as {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {e}")


# Create main window
root = tk.Tk()

# Change background color
root.configure(bg="white")

root.title("CSV to Excel Converter")
root.geometry("600x600")

# Create upload button with custom colors
upload_button = tk.Button(
    root, 
    text="Upload CSV File", 
    command=upload_and_convert, 
    bg="#4CAF50",  # Button background color
    fg="white",    # Button text color
    font=("Helvetica", 12, "bold")  # Button font
)
upload_button.pack(pady=200)

# Create save button (initially disabled) with custom colors
save_button = tk.Button(
    root, 
    text="Save Excel File", 
    command=save_excel, 
    state=tk.DISABLED, 
    bg="#2196F3",  # Button background color
    fg="white",    # Button text color
    font=("Helvetica", 12, "bold")  # Button font
)
save_button.pack(pady=30)

# Initialize converted_df as None
converted_df = None

root.mainloop()
