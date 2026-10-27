!pip install pillow
from PIL import Image, ImageDraw, ImageFont
txt=input("Enter Your Text: ")
image=Image.new("RGB", (800,300), "white")
draw=ImageDraw.Draw(image)
font=ImageFont.load_default()   
draw.text( (50,100) , txt, fill="black",font=font)
image.save("Generated_Text_Image.png")
print("Image Generated Successfully!")
