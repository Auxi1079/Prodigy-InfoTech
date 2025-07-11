# 🖼️ Image Encryption Tool in Python

This is a simple Python program that allows users to **encrypt and decrypt images** using basic pixel level manipulation. It uses the XOR operation on each pixel with a secret key, making the process reversible and lightweight.

## 🔐 How It Works

- Each pixel (R, G, B) value in the image is XORed with a numeric key (0–255)
- Applying the same key again decrypts the image (XOR is symmetric)
- Works with most image formats (JPG, PNG, etc.)

## 📦 Features

• Encrypt any image file using a numeric key  
• Decrypt the encrypted image using the same key  
• Uses XOR operation for fast, reversible encryption  
• Easy to use command line interface  
• Built with Python and Pillow (PIL)

## ▶️ How to Run

1. Make sure Python 3 and Pillow are installed:
```bash
pip install Pillow
