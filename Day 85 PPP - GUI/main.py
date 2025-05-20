# Professional Portfolio Project - GUI
# Image Watermaking Desktop App
# Author : Abraham
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        self.label = tk.Label(root, text="Enter watermark text:")
        self.label.pack()

        self.text_entry = tk.Entry(root, width=40)
        self.text_entry.pack()

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.add_watermark_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_watermark_btn.pack(pady=5)

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_btn.pack(pady=5)

        self.original_image = None
        self.watermarked_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = Image.open(file_path).convert("RGBA")
            self.display_image(self.original_image)

    def display_image(self, img):
        img = img.resize((400, 400), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.canvas.img_tk = img_tk
        self.canvas.create_image(250, 250, image=img_tk)

    def add_watermark(self):
        if not self.original_image:
            return

        watermark_text = self.text_entry.get()
        image = self.original_image.copy()
        draw = ImageDraw.Draw(image)

        # You can use your own .ttf font file here
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()

        width, height = image.size
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]


        # Add text in bottom right
        position = (width - text_width - 10, height - text_height - 10)

        draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

        self.watermarked_image = image
        self.display_image(image)

    def save_image(self):
        if self.watermarked_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                self.watermarked_image.convert("RGB").save(save_path)
                tk.messagebox.showinfo("Saved", "Image saved successfully!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
