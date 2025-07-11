from PIL import Image

def encrypt_image(input_path, output_path, key=10):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print(f"Encrypted image saved as: {output_path}")

def decrypt_image(input_path, output_path, key=10):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)

    img.save(output_path)
    print(f"Decrypted image saved as: {output_path}")

# Run this
encrypt_image("original.jpg", "encrypted.png")
decrypt_image("encrypted.png", "decrypted.png")
