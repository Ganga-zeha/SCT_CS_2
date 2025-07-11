SCT_CS_2 - Image Encryption Tool

This is Task 2 of the Cyber Security Internship at SkillCraft Technology.

Task Description
-Build a tool that encrypts and decrypts images using pixel manipulation techniques.

Features:
- Encrypts an image by altering RGB pixel values using a key
- Decrypts the image to restore the original
- Works with `.jpg`, `.png`, etc.

How it works:
- Adds a key (e.g., +10) to every R, G, B value during encryption
- Subtracts the same key (e.g., -10) to decrypt

Requirements:
- Python
- Pillow library

bash
pip install pillow

How to run:
python image_encryptor.py
