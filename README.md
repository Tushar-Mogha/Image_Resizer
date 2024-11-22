# Image Resizer

This is a Python-based graphical application for resizing images. The application features a user-friendly interface that allows users to select an image, preview it, specify dimensions, and save the resized image to a selected output directory.

---

## Features

1. **Image Selection**:
   - Browse and select an image file (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`).
   - Preview the selected image in the application.

2. **Resizable Dimensions**:
   - Specify custom width and height for the resized image.

3. **Output Directory**:
   - Choose the destination folder for saving resized images.

4. **Real-time Image Preview**:
   - Displays a preview of the selected image in a fixed-sized preview area.

5. **User-friendly Design**:
   - Clean and modern GUI with intuitive controls.

---

## Technologies Used

- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Image Processing**: PIL (Python Imaging Library) via the `Pillow` module

---

## Prerequisites

Ensure you have the following installed on your system:

1. **Python 3.6 or above**
2. **Required Python libraries**:
   - `Pillow`
   - `tkinter` (usually included with Python installations)

Install the required library using pip:

- pip install pillow

## How to Use

1. **Run the Script**:
   - Save the script as `image_resizer.py` and execute it:
     ```bash
     python image_resizer.py
     ```

2. **Select an Image**:
   - Click the **Browse** button next to "Select Image" to choose an image file from your system.
   - The selected image will be displayed in the preview area.

3. **Specify Output Directory**:
   - Click the **Browse** button next to "Output Directory" to select the folder where the resized image will be saved.

4. **Enter Dimensions**:
   - Specify the desired width and height for the resized image in the corresponding fields.

5. **Resize the Image**:
   - Click the **Resize Image** button to resize the selected image and save it to the specified output directory.

6. **Success Notification**:
   - A success message will appear upon successful resizing and saving of the image.

---

## File Structure

---

## Preview

### GUI Layout


![Screenshot 2024-11-22 170323](https://github.com/user-attachments/assets/714ba867-e1ca-44b2-83de-430d781024c9)



![Screenshot 2024-11-22 170358](https://github.com/user-attachments/assets/91b68802-6562-4b4f-879a-7785a090c3ee)




---

## Error Handling

- The application prevents non-image files from being selected.
- Ensures that the width and height inputs are valid integers.
- Displays detailed error messages for invalid inputs or unexpected issues during execution.

---
