from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def resize_image(input_path, output_dir, width, height):
    """
    Resizes a single image to the specified dimensions
    and saves it to the output directory.
    
    Parameters:
    - input_path (str): Path to the input image.
    - output_dir (str): Path to the directory to save the resized image.
    - width (int): Target width of the resized image.
    - height (int): Target height of the resized image.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_name = os.path.basename(input_path)
    output_path = os.path.join(output_dir, file_name)
    
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            messagebox.showinfo("Success", f"Image resized and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize image: {e}")

def browse_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        input_path_entry.delete(0, tk.END)
        input_path_entry.insert(0, file_path)
        show_image(file_path)

def browse_output_dir():
    directory = filedialog.askdirectory(title="Select Output Directory")
    if directory:
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(0, directory)

def show_image(image_path):
    try:
        with Image.open(image_path) as img:
            img.thumbnail((300, 300))  # Maintain a consistent preview size
            img = ImageTk.PhotoImage(img)
            image_preview_label.config(image=img)
            image_preview_label.image = img
            image_preview_label_text.pack_forget()  # Hide placeholder text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")

def start_resizing():
    input_path = input_path_entry.get()
    output_dir = output_dir_entry.get()
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Width and Height must be integers.")
        return

    if not os.path.isfile(input_path):
        messagebox.showerror("Invalid Input", "Please select a valid image file.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    resize_image(input_path, output_dir, width, height)

# Tkinter GUI
root = tk.Tk()
root.title("Image Resizer")
root.geometry("600x600")
root.configure(bg="#f7f7f7")

# Input Image
tk.Label(root, text="Select Image:", bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
input_path_entry = tk.Entry(root, width=40, font=("Arial", 10))
input_path_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_image, bg="#4CAF50", fg="white", font=("Arial", 10)).grid(row=0, column=2, padx=10, pady=10)

# Image Preview
image_preview_frame = tk.Frame(root, bg="#ffffff", relief="sunken", width=300, height=300)
image_preview_frame.grid(row=1, column=0, columnspan=3, pady=10)
image_preview_frame.grid_propagate(False)

image_preview_label = tk.Label(image_preview_frame, bg="#ffffff")
image_preview_label.pack(expand=True)

image_preview_label_text = tk.Label(
    image_preview_frame, text="Image Preview", bg="#ffffff", font=("Arial", 10), fg="#aaaaaa"
)
image_preview_label_text.pack()

# Output Directory
tk.Label(root, text="Output Directory:", bg="#f7f7f7", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
output_dir_entry = tk.Entry(root, width=40, font=("Arial", 10))
output_dir_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_dir, bg="#4CAF50", fg="white", font=("Arial", 10)).grid(row=2, column=2, padx=10, pady=10)

# Target Dimensions
tk.Label(root, text="Width:", bg="#f7f7f7", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky="e")
width_entry = tk.Entry(root, width=10, font=("Arial", 10))
width_entry.grid(row=3, column=1, sticky="w", padx=10)

tk.Label(root, text="Height:", bg="#f7f7f7", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(root, width=10, font=("Arial", 10))
height_entry.grid(row=4, column=1, sticky="w", padx=10)

# Start Button
tk.Button(
    root, text="Resize Image", command=start_resizing, bg="#2196F3", fg="white", font=("Arial", 12), width=20
).grid(row=5, column=0, columnspan=3, pady=20)

root.mainloop()
