import os

def combine():
    image_file = input("Image file: ")
    zip_file = input("ZIP file: ")
    image_name, image_ext = os.path.splitext(image_file)
    output_file = f"{image_name}_combined{image_ext}"

    try:
        with open(image_file, 'rb') as img, open(zip_file, 'rb') as zipf:
            img_data = img.read()
            zip_data = zipf.read()

        with open(output_file, 'wb') as output:
            output.write(img_data)
            output.write(zip_data)

        print(f"Check output at: {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    combine()