import binascii
from tkinter import Tk, Label, Button, Text, filedialog, messagebox
from PIL import Image, ImageTk

# Function to convert image to hex code
def image_to_hex(image_path):
    with open(image_path, 'rb') as image_file:
        hex_data = binascii.hexlify(image_file.read())
    return hex_data

# Function to convert hex code back to image
def hex_to_image(hex_data, output_path):
    with open(output_path, 'wb') as image_file:
        image_file.write(binascii.unhexlify(hex_data))

# Function to add hidden data (append to the end)
def add_hidden_data(hex_data, hidden_data):
    return hex_data + binascii.hexlify(hidden_data.encode())

# Function to extract hidden data
def extract_hidden_data(hex_data, original_length):
    hidden_hex = hex_data[original_length:]
    hidden_data = binascii.unhexlify(hidden_hex).decode(errors='ignore')
    return hidden_data

# Load original image
def load_image():
    global original_image_path, original_image_hex, original_length

    original_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if original_image_path:
        original_image_hex = image_to_hex(original_image_path)
        print(f"original Image Hex: {original_image_hex}")
        original_length = len(original_image_hex)

        original_image = Image.open(original_image_path)
        original_image_tk = ImageTk.PhotoImage(original_image)
        original_image_label.config(image=original_image_tk)
        original_image_label.image = original_image_tk
        messagebox.showinfo("Image Loaded", "Original image loaded successfully!")

# Embed hidden message
def embed_message():
    global modified_image_hex, original_length

    hidden_message = message_entry.get("1.0", "end-1c")
    if not hidden_message:
        messagebox.showwarning("No Message", "Please enter a message to embed.")
        return

    modified_image_hex = add_hidden_data(original_image_hex, hidden_message)
    print(f"Modified Image Hex: {modified_image_hex}")
    hex_to_image(modified_image_hex, 'modified_image.png')
    original_length = len(original_image_hex)  # Store the original length for extraction

    modified_image = Image.open('modified_image.png')
    modified_image_tk = ImageTk.PhotoImage(modified_image)
    modified_image_label.config(image=modified_image_tk)
    modified_image_label.image = modified_image_tk
    messagebox.showinfo("Message Embedded", "Message embedded successfully!")

# Extract hidden message
def extract_message():
    try:
        # Load the modified image's hex data
        modified_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if modified_image_path:
            modified_image_hex = image_to_hex(modified_image_path)

            # Ensure the original length is known; if not, ask the user to provide it
            if 'original_length' not in globals():
                messagebox.showwarning("Warning", "Please embed a message before extracting it, or reload the original image.")
                return

            hidden_message = extract_hidden_data(modified_image_hex, original_length)
            messagebox.showinfo("Extracted Message", f"Hidden Message: {hidden_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract message: {e}")

# Save original or modified image
def save_image(image_type):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if save_path:
        try:
            if image_type == 'original':
                with open(original_image_path, 'rb') as src_file:
                    with open(save_path, 'wb') as dst_file:
                        dst_file.write(src_file.read())
            elif image_type == 'modified':
                hex_to_image(modified_image_hex, save_path)
            messagebox.showinfo("Image Saved", f"{image_type.capitalize()} image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save {image_type} image: {e}")

# GUI setup
root = Tk()
root.title("Steganography Simulator")

# Load original image
load_button = Button(root, text="Load Image", command=load_image)
load_button.pack(pady=10)

# Display original image
original_image_label = Label(root)
original_image_label.pack(side="left", padx=10)

# Display modified image
modified_image_label = Label(root)
modified_image_label.pack(side="right", padx=10)

# Entry for hidden message
Label(root, text="Enter Message to Embed:").pack(pady=10)
message_entry = Text(root, height=4, width=40)
message_entry.pack(pady=10)

# Embed message button
embed_button = Button(root, text="Embed Message", command=embed_message)
embed_button.pack(pady=5)

# Extract message button
extract_button = Button(root, text="Extract Message from Saved Image", command=extract_message)
extract_button.pack(pady=5)

# Save original or modified image buttons
save_original_button = Button(root, text="Save Original Image", command=lambda: save_image('original'))
save_original_button.pack(pady=5)
save_modified_button = Button(root, text="Save Modified Image", command=lambda: save_image('modified'))
save_modified_button.pack(pady=5)

root.mainloop()
