# Image Encryption Tool

## Overview
This tool allows you to encrypt and decrypt images using a secure, reversible pixel manipulation method (XOR cipher combined with pixel shuffling). It features a modern, user-friendly graphical interface for easy operation.

## Features
- **Encrypt images** with a user-provided key (0-255)
- **Decrypt images** using the same key to restore the original
- **Modern, clean GUI** built with Python's Tkinter and ttk
- **No need to type file paths** – use file pickers for input and output
- **Input fields are cleared after each operation** for a smooth workflow
- **Clear instructions and feedback** throughout the process

## How It Works
- The tool applies an XOR operation to each pixel's RGB values using your chosen key.
- Then, it shuffles the pixel positions in a way that only the same key can reverse.
- The encrypted image appears as total noise—no shapes, outlines, or colors from the original are visible.
- Decrypting with the same key perfectly restores the original image.

## Installation
1. Make sure you have Python 3 installed.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the tool:
   ```sh
   python image_encryptor.py
   ```
2. The GUI will appear. Follow these steps:
   - **Mode:** Choose 'Encrypt' or 'Decrypt'.
   - **Key:** Enter a number between 0 and 255. Remember this key!
   - **Input Image:** Click 'Browse' to select the image you want to process.
   - **Output Image:** Click 'Browse' to choose where to save the result and give it a name (e.g., `encrypted.png`).
   - **Run:** Click the 'Run' button. A message will confirm success or show any errors.
   - **After each operation, all fields are cleared** so you can easily start a new task.

## Example Workflow
- To encrypt: Select your image, choose 'Encrypt', enter a key, pick an output file, and click Run.
- To decrypt: Select the encrypted image, choose 'Decrypt', enter the same key, pick an output file, and click Run.

## Encryption Method
- **XOR Cipher:** Each pixel's R, G, and B values are XOR'd with the key.
- **Pixel Shuffling:** The positions of all pixels are shuffled in a way that only the same key can reverse.
- **Result:** The encrypted image is completely scrambled and unrecognizable. Decryption with the same key restores the original image exactly.
- **Security Note:** This method is for educational purposes and is not secure for protecting sensitive images against determined attackers.

## Project Requirements Fulfilled
- [x] **Encrypt and decrypt images using pixel manipulation**
- [x] **User-friendly interface (no command line required)**
- [x] **Reversible process (original image is restored with the same key)**
- [x] **Modern, clean, and interactive GUI**
- [x] **Encrypted image is fully scrambled and unrecognizable**
- [x] **Input fields clear after each operation**
- [x] **Well-documented usage and workflow**

## License
This project is provided for educational purposes.