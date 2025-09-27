from PIL import Image, ImageDraw, ImageFont
import subprocess

DEVICE_ID = "[your id]"  
IMAGE_FILE = "text.png"  
FONT_SIZE = 24  

def text_to_image(text, font_size=24):
    try:
        font = ImageFont.truetype("Arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    
    temp_img = Image.new("L", (1, 1), color=255)
    draw = ImageDraw.Draw(temp_img)
    bbox = draw.textbbox((0, 0), text, font=font)
    
    width = 384 
    height = bbox[3] - bbox[1] + 10 
    
    image = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 0), text, font=font, fill=0)
    return image

img = text_to_image("Hello, Cat Printer! This is a test.", FONT_SIZE)
img.save(IMAGE_FILE)

print("Sending image to printer...")
try:
    subprocess.run(["python3", "print.py", "--device", DEVICE_ID, IMAGE_FILE],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Done!")
except subprocess.CalledProcessError:
    print("Failed to send the image to the printer.")
