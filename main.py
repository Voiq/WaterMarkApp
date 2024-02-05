from tkinter import *
from PIL import Image, ImageTk,ImageDraw,ImageFont
from tkinter import filedialog


#-------------------------#
FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
image_path=None

#-------------------------Functions-----------------------#
def upload_image():
    global image_path
    file_path=filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_path=file_path
        image = Image.open(file_path)
        tk_image=ImageTk.PhotoImage(image)
        image_label.config(image=tk_image)
        image_label.image = tk_image


def apply_watermark():
    global image_path
    
    if image_path:

        original_image=Image.open(image_path).convert("RGBA")

        watermarked_image=original_image.copy()

        font = ImageFont.load_default()

        draw = ImageDraw.Draw(watermarked_image)

        image_width,image_height = original_image.size

        watermark_text="Watermark Test"

        x_position = image_width - 125
        y_position = image_height - 125
        watermark_color=(255, 255, 255, 128)

        draw.text((x_position, y_position), watermark_text, font=font, fill=watermark_color)

        watermarked_image.save("E:\Projects\WaterMarkApp\image_with_watermark.png")

#-------------------------UI-----------------------#

window = Tk()
window.title("Watermarker")
window.config(padx=50 ,pady=50,bg=YELLOW)


#placeholder
image_label=Label()
image_label.grid(column=1,row=1)


upload_button = Button(text="Upload an Image" , font=(FONT_NAME,15,"bold"),highlightthickness=0,command=upload_image)
upload_button.grid(column=0,row=2)



apply_button= Button(text="Apply Watermark" , font=(FONT_NAME,15,"bold"),highlightthickness=0,command=apply_watermark)
apply_button.grid(column=2,row=2)



window.mainloop()

