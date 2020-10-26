from PIL import Image, ImageFont, ImageDraw

bg = Image.open("maymay.jpg")

width = bg.width
height = bg.height

fonttype = ImageFont.truetype("impact.ttf",20)

drawingarea = ImageDraw.Draw(bg)

text = "Got just one of these\nAlready the richest in the hood"
text_width, text_height = drawingarea.textsize(text, font=fonttype)
print("tekstbreedte=" + str(text_width) + ", tekst_hoogte=" + str(text_height))
text_x = (width - text_width) / 2
text_y = (height - text_height) / 2

drawingarea.multiline_text((text_x,text_y), text, font=fonttype, fill=(0,0,0))
drawingarea.multiline_text((text_x-3, text_y-3), text, font=fonttype, fill=(255,255,255))

bg.show()

bg.save("maymay_with_text.jpg")