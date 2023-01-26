from PIL import Image, ImageDraw, ImageFont

# Firstly we need to open an image
greeting_card_img = Image.open('Greeting Card.jpg')

# Enabling drawing on this card
img_drawer = ImageDraw.Draw(greeting_card_img)

# Loading my own custom font style and size
custom_font = ImageFont.truetype('Sinthya-jlYM.ttf', 62)

# Now we can draw the text on the image using the img_drawer
img_drawer.text((230, 170), "Happy  Anniversary !", font = custom_font, fill = (255, 0, 0))
img_drawer.text((230, 270), "Beautiful Human", font = custom_font, fill = (255, 0, 0))

# We can either display or save the image
greeting_card_img.show()

# We save the image now
greeting_card_img.save('S20200010042_greeting-card.jpg')