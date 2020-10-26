from PIL import Image

meme = Image.open("meme.png")

meme.show()

width = meme.width
height = meme.height

half_width = width // 2
half_height = height // 2

new_size = (half_width, half_height)
smaller_meme = meme.resize(new_size)
smaller_meme.save("meme_small.jpg")

