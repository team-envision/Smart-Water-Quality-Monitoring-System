import os
import logging
from PIL import Image

input_folder = r"algae"
output_folder = r"insect"

# Create a logger object to log errors and warnings
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
handler = logging.FileHandler('image_converter.log')
handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



for filename in os.listdir(input_folder):
    if filename.endswith(".jpeg"):
        try:
            # Open the image using Pillow
            image = Image.open(os.path.join(input_folder, filename))

            # Convert the image to RGB format
            rgb_image = image.convert("RGB")

            # Save the JPG image to the output folder
            output_filename = filename.replace(".jpeg", ".jpg")
            rgb_image.save(os.path.join(output_folder, output_filename), quality=50)
        except Exception as e:
            print(f"Error converting {filename}: {e}")
    elif filename.endswith(".jpg"):
        try:
            # Open the image using Pillow
            image = Image.open(os.path.join(input_folder, filename))

            # Convert the image to RGB format
            rgb_image = image.convert("RGB")

            # Save the JPG image to the output folder
            rgb_image.save(os.path.join(output_folder, filename), quality=50)
        except Exception as e:
            print(f"Error converting {filename}: {e}")


input_folder = r"insect"
output_folder = r"palgae"


# Loop through all the JPEG images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        try:
            # Open the image using Pillow
            image = Image.open(os.path.join(input_folder, filename))

            # Convert the image to RGBA format
            rgba_image = image.convert("RGBA")

            # Reduce the size of the PNG image
            png_image = rgba_image.save(os.path.join(output_folder, filename.replace(".jpg" or ".jpeg", ".png")), optimize=True, quality=50)

            # Check if the save() method succeeded
            if png_image:
                # Save the PNG image to the output folder
                png_image.save(os.path.join(output_folder, filename.replace(".jpg" or ".jpeg", ".png")), optimize=True, quality=50)
        except FileNotFoundError:
            logger.warning(f"File {filename} not found in input folder")
        except Exception as e:
            logger.error(f"Error converting {filename}: {e}")