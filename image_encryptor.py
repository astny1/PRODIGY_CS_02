import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os
import random

def load_image(path):
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def encrypt_image(image, key):
    image = image.convert('RGB')
    width, height = image.size
    pixels = list(image.getdata())
    # XOR each pixel
    xor_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]
    # Shuffle pixel positions deterministically using the key
    indices = list(range(len(xor_pixels)))
    rng = random.Random(key)
    rng.shuffle(indices)
    shuffled_pixels = [None] * len(xor_pixels)
    for i, idx in enumerate(indices):
        shuffled_pixels[idx] = xor_pixels[i]
    encrypted_img = Image.new('RGB', (width, height))
    encrypted_img.putdata(shuffled_pixels)
    return encrypted_img

def decrypt_image(image, key):
    image = image.convert('RGB')
    width, height = image.size
    pixels = list(image.getdata())
    # Unshuffle pixel positions deterministically using the key
    indices = list(range(len(pixels)))
    rng = random.Random(key)
    rng.shuffle(indices)
    unshuffled_pixels = [None] * len(pixels)
    for i, idx in enumerate(indices):
        unshuffled_pixels[i] = pixels[idx]
    # XOR each pixel to decrypt
    orig_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in unshuffled_pixels]
    decrypted_img = Image.new('RGB', (width, height))
    decrypted_img.putdata(orig_pixels)
    return decrypted_img

def gui_main():
    def select_input():
        path = filedialog.askopenfilename(title='Select input image', filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if path:
            input_path_var.set(path)

    def select_output():
        path = filedialog.asksaveasfilename(title='Save output image as', defaultextension='.png', filetypes=[('PNG Image', '*.png'), ('JPEG Image', '*.jpg;*.jpeg'), ('Bitmap Image', '*.bmp'), ('GIF Image', '*.gif')])
        if path:
            output_path_var.set(path)

    def process():
        mode = mode_var.get()
        input_path = input_path_var.get()
        output_path = output_path_var.get()
        try:
            key = int(key_var.get())
            if not (0 <= key <= 255):
                raise ValueError
        except ValueError:
            messagebox.showerror('Error', 'Key must be an integer between 0 and 255.')
            return
        if not os.path.isfile(input_path):
            messagebox.showerror('Error', 'Input image file does not exist.')
            return
        try:
            image = load_image(input_path)
            if mode == 'Encrypt':
                result = encrypt_image(image, key)
            else:
                result = decrypt_image(image, key)
            save_image(result, output_path)
            messagebox.showinfo('Success', f'Image {mode.lower()}ed and saved to:\n{output_path}')
            # Clear fields after operation
            input_path_var.set("")
            output_path_var.set("")
            key_var.set("")
        except Exception as e:
            messagebox.showerror('Error', f'Failed to process image:\n{e}')

    root = tk.Tk()
    root.title('Image Encryption Tool')
    root.geometry('440x320')
    root.resizable(False, False)
    style = ttk.Style(root)
    style.theme_use('clam')
    style.configure('TFrame', background='#f4f6fb')
    style.configure('TLabel', background='#f4f6fb', font=('Segoe UI', 11))
    style.configure('TEntry', font=('Segoe UI', 10))
    style.configure('TCombobox', font=('Segoe UI', 10))

    mode_var = tk.StringVar(value='Encrypt')
    input_path_var = tk.StringVar()
    output_path_var = tk.StringVar()
    key_var = tk.StringVar()

    main_frame = ttk.Frame(root, padding=30, style='TFrame')
    main_frame.pack(fill='both', expand=True)

    ttk.Label(main_frame, text='Image Encryption Tool', font=('Segoe UI', 18, 'bold'), background='#f4f6fb', foreground='#222').pack(pady=(0, 18))

    form_frame = ttk.Frame(main_frame, style='TFrame')
    form_frame.pack(fill='x', pady=5)

    # Mode
    ttk.Label(form_frame, text='Mode:').grid(row=0, column=0, sticky='w', pady=8, padx=(0,8))
    mode_combo = ttk.Combobox(form_frame, textvariable=mode_var, values=['Encrypt', 'Decrypt'], state='readonly', width=12)
    mode_combo.grid(row=0, column=1, sticky='w', padx=(0,16))

    # Key
    ttk.Label(form_frame, text='Key (0-255):').grid(row=0, column=2, sticky='w', padx=(0,8))
    key_entry = ttk.Entry(form_frame, textvariable=key_var, width=10)
    key_entry.grid(row=0, column=3, sticky='w')

    # Input Image
    ttk.Label(form_frame, text='Input Image:').grid(row=1, column=0, sticky='w', pady=8, padx=(0,8))
    input_entry = ttk.Entry(form_frame, textvariable=input_path_var, width=28)
    input_entry.grid(row=1, column=1, columnspan=2, sticky='we', padx=(0,8))
    input_browse = ttk.Button(form_frame, text='Browse', command=select_input)
    input_browse.grid(row=1, column=3, sticky='w')

    # Output Image
    ttk.Label(form_frame, text='Output Image:').grid(row=2, column=0, sticky='w', pady=8, padx=(0,8))
    output_entry = ttk.Entry(form_frame, textvariable=output_path_var, width=28)
    output_entry.grid(row=2, column=1, columnspan=2, sticky='we', padx=(0,8))
    output_browse = ttk.Button(form_frame, text='Browse', command=select_output)
    output_browse.grid(row=2, column=3, sticky='w')

    # Run button with label
    ttk.Label(main_frame, text='Click to start encryption or decryption.', font=('Segoe UI', 10, 'italic'), background='#f4f6fb', foreground='#333').pack(pady=(24, 4))
    run_btn = ttk.Button(main_frame, text='Run', command=process)
    run_btn.pack(ipadx=20, ipady=8)

    root.mainloop()

if __name__ == '__main__':
    gui_main()