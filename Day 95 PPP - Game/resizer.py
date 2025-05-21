from PIL import Image

# Open original image
img = Image.open("invader.gif")

# Resize it to smaller dimensions (e.g., 30x30)
img = img.resize((30, 30), Image.LANCZOS)

# Save as new GIF
img.save("invader_small.gif")
