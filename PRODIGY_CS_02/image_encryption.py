from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        img = img.convert("RGB")
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        print(f"Image encrypted and saved as: {output_path}")

    except Exception as e:
        print("Error during encryption:", e)

def decrypt_image(input_path, output_path, key):
    # Decryption is identical to encryption with XOR
    encrypt_image(input_path, output_path, key)

def main():
    print("=== Image Encryption Tool ===")

    while True:
        choice = input("Choose an option (encrypt / decrypt / exit): ").strip().lower()

        if choice in ["encrypt", "decrypt"]:
            in_path = input("Enter the path to the image: ").strip()
            out_path = input("Enter the output image path: ").strip()
            key = int(input("Enter a numeric key (0–255): ").strip())

            if not os.path.exists(in_path):
                print("Input image not found.")
                continue

            if not (0 <= key <= 255):
                print("Key must be between 0 and 255.")
                continue

            if choice == "encrypt":
                encrypt_image(in_path, out_path, key)
            else:
                decrypt_image(in_path, out_path, key)

        elif choice == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose 'encrypt', 'decrypt', or 'exit'.")

if __name__ == "__main__":
    main()
