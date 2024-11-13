import binascii
from tkinter import Tk, Label, Button, Text, filedialog, messagebox, Canvas, Scrollbar, Frame
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
    global original_image_path, original_image_hex, original_length, original_image_tk

    original_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    if original_image_path:
        original_image_hex = image_to_hex(original_image_path).decode()
         # Define the file name
        file_name = "original_image_hex.txt"

        # Create and write the hex data to the file
        with open(file_name, "w") as file:
            file.write(original_image_hex)

        print(f"Hex data written to {file_name}")
        
        original_length = len(original_image_hex)
        
        # Load and resize image for display
        original_image = Image.open(original_image_path)
        original_image = original_image.resize((200, 200), Image.ANTIALIAS)  # Resize for smaller displays
        original_image_tk = ImageTk.PhotoImage(original_image)

        # Display in the canvas
        original_canvas.create_image(0, 0, image=original_image_tk, anchor="nw")
        original_canvas.config(scrollregion=original_canvas.bbox("all"))
        messagebox.showinfo("Image Loaded", "Original image loaded successfully!")

# Embed hidden message
def embed_message():
    global modified_image_hex, original_length, modified_image_tk

    hidden_message = message_entry.get("1.0", "end-1c")
    if not hidden_message:
        messagebox.showwarning("No Message", "Please enter a message to embed.")
        return

    modified_image_hex = add_hidden_data(original_image_hex.encode(), hidden_message).decode()
    # Convert modified_image_hex to a string if it is in bytes
    if isinstance(modified_image_hex, bytes):
        modified_image_hex = modified_image_hex.decode()  # Converts bytes to a hex string

    file_name = "modified_image_hex.txt"

    # Create and write the hex data to the file
    with open(file_name, "w") as file:
        file.write(modified_image_hex)

    hex_to_image(modified_image_hex.encode(), 'modified_image.png')

    modified_image = Image.open('modified_image.png')
    modified_image = modified_image.resize((200, 200), Image.ANTIALIAS)
    modified_image_tk = ImageTk.PhotoImage(modified_image)

    # Display in the canvas
    modified_canvas.create_image(0, 0, image=modified_image_tk, anchor="nw")
    modified_canvas.config(scrollregion=modified_canvas.bbox("all"))
    messagebox.showinfo("Message Embedded", "Message embedded successfully!")

# Extract hidden message
def extract_message():
    try:
        modified_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if modified_image_path:
            modified_image_hex = image_to_hex(modified_image_path).decode()
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

# Canvas for original image with scrollbars
original_frame = Frame(root)
original_frame.pack(side="left", padx=10, pady=10)
original_canvas = Canvas(original_frame, width=200, height=200)
original_canvas.pack(side="left")
scroll_y_orig = Scrollbar(original_frame, orient="vertical", command=original_canvas.yview)
scroll_y_orig.pack(side="right", fill="y")
original_canvas.config(yscrollcommand=scroll_y_orig.set)
Label(root, text="Original Image").pack(side="left")

# Canvas for modified image with scrollbars
modified_frame = Frame(root)
modified_frame.pack(side="right", padx=10, pady=10)
modified_canvas = Canvas(modified_frame, width=200, height=200)
modified_canvas.pack(side="left")
scroll_y_mod = Scrollbar(modified_frame, orient="vertical", command=modified_canvas.yview)
scroll_y_mod.pack(side="right", fill="y")
modified_canvas.config(yscrollcommand=scroll_y_mod.set)
Label(root, text="Modified Image").pack(side="right")

# Entry for hidden message
Label(root, text="Enter Message to Embed:").pack(pady=10)
message_entry = Text(root, height=4, width=40)
message_entry.pack(pady=10)

# Buttons
load_button = Button(root, text="Load Image", command=load_image)
load_button.pack(pady=5)
embed_button = Button(root, text="Embed Message", command=embed_message)
embed_button.pack(pady=5)
extract_button = Button(root, text="Extract Message", command=extract_message)
extract_button.pack(pady=5)
# Save original or modified image buttons
save_original_button = Button(root, text="Save Original Image", command=lambda: save_image('original'))
save_original_button.pack(pady=5)
save_modified_button = Button(root, text="Save Modified Image", command=lambda: save_image('modified'))
save_modified_button.pack(pady=5)


root.mainloop()
