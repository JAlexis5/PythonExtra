from PIL import Image

meme = Image.open("meme.png")

meme.show()

width = meme.width
height = meme.height

print("Image width in px = " + str(width) + ", Image height in px = " + str(height))

print(meme.format , meme.size , meme.mode)