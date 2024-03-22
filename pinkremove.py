from PIL import Image
import glob
import os



images = glob.glob("./converts/**/*.png", recursive=True)


cur_count = 0

def remove_pink(image_path,):
    # Open the image
    img = Image.open(image_path)
    img = img.convert("RGBA")

    # Get the image data as a list of tuples
    img_data = list(img.getdata())

    # Iterate over each pixel
    for i, pixel in enumerate(img_data):
        if pixel[0] == 255 and pixel[1] == 0 and pixel[2] == 255:  # Pink color (R=255, G=0, B=255)
            img_data[i] = (255, 255, 255, 0)  # Make it transparent

    # Update the image with the modified data
    img.putdata(img_data)

    
    img.save(image_path, "PNG")


for image in images:
    remove_pink(image)