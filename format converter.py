import os
import logging
from PIL import Image

<<<<<<< HEAD
input_folder = r"C:\Users\Sahil Sahu\Desktop\Smart-Water-Quality-Monitoring-System\algae"
output_folder = r"C:\Users\Sahil Sahu\Desktop\Smart-Water-Quality-Monitoring-System\palgae"
=======
input_folder = r"algae"
output_folder = r"insect"
>>>>>>> 295fdc7e74f399f7e01e8ca88f6d0b7ec8c0bc68

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


<<<<<<< HEAD
# input_folder = r"C:\Users\Sahil Sahu\Desktop\Smart-Water-Quality-Monitoring-System\algae"
# output_folder = r"C:\Users\Sahil Sahu\Desktop\Smart-Water-Quality-Monitoring-System\palgae"
=======
input_folder = r"insect"
output_folder = r"palgae"
>>>>>>> 295fdc7e74f399f7e01e8ca88f6d0b7ec8c0bc68

target_size = (256, 256)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        try:
            # Open the image using Pillow
            image = Image.open(os.path.join(input_folder, filename))

            # Get the original image size
            width, height = image.size

            # Find the larger dimension
            larger_dim = max(width, height)

            # Calculate the scaling factor
            scale_factor = target_size[0] / larger_dim

            # Calculate the new size
            new_size = (int(scale_factor * width), int(scale_factor * height))

            # Resize the image
            image = image.resize(new_size, resample=Image.LANCZOS)

            # Create a blank background image of target size
            background = Image.new('RGB', target_size, (255, 255, 255))

            # Paste the resized image on the center of background image
            offset = ((target_size[0] - new_size[0]) // 2, (target_size[1] - new_size[1]) // 2)
            background.paste(image, offset)

            # Save the image to the output folder
            background.save(os.path.join(output_folder, filename), optimize=True, quality=50)

        except FileNotFoundError:
            print(f"File {filename} not found in input folder")
        except Exception as e:
            print(f"Error converting {filename}: {e}")

input_folder = r"palgae"
output_folder = r"png_allok"

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