from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def resize_images_in_directory(input_dir, output_dir, width, height):
    """
    Resizes all images in the input directory to the specified dimensions
    and saves them to the output directory.

    Parameters:
    - input_dir (str): Path to the directory containing input images.
    - output_dir (str): Path to the directory to save resized images.
    - width (int): Target width of the resized images.
    - height (int): Target height of the resized images.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                with Image.open(input_path) as img:
                    resized_img = img.resize((width, height))
                    resized_img.save(output_path)
            except Exception as e:
                print(f"Error resizing {input_path}: {e}")

def browse_input_dir():
    directory = filedialog.askdirectory(title="Select Input Directory")
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(0, directory)

def browse_output_dir():
    directory = filedialog.askdirectory(title="Select Output Directory")
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, directory)

def start_resizing():
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Width and Height must be integers.")
        return

    if not os.path.exists(input_dir):
        messagebox.showerror("Invalid Input", "Input directory does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    resize_images_in_directory(input_dir, output_dir, width, height)
    messagebox.showinfo("Success", "Images resized successfully!")

# Tkinter GUI
root = tk.Tk()
root.title("Image Resizer")

# Input Directory
tk.Label(root, text="Input Directory:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
input_dir_entry = tk.Entry(root, width=50)
input_dir_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_input_dir).grid(row=0, column=2, padx=10, pady=10)

# Output Directory
tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_dir).grid(row=1, column=2, padx=10, pady=10)

# Target Dimensions
tk.Label(root, text="Width:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
width_entry = tk.Entry(root, width=10)
width_entry.grid(row=2, column=1, sticky="w", padx=10)

tk.Label(root, text="Height:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(root, width=10)
height_entry.grid(row=3, column=1, sticky="w", padx=10)

# Start Button
tk.Button(root, text="Resize Images", command=start_resizing, bg="lightblue").grid(row=4, column=1, pady=20)

root.mainloop()
