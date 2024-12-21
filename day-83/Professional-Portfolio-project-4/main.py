import tkinter as tk

from tkinter import filedialog, messagebox

from PIL import Image, ImageDraw, ImageFont, ImageTk



class WatermarkApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Image Watermarking App")

        self.root.geometry("800x600")

        self.root.minsize(800, 600)

        self.root.resizable(True, True)

        try:

            self.root.iconbitmap("app_icon.ico")

        except:

            pass

        self.image = None

        self.watermarked_image = None

        self.filepath = None

        self.bg_color = "#f0f0f0"

        self.button_color = "#4CAF50"

        self.hover_color = "#45a049"

        self.label_color = "#333333"

        self.button_font = ("Helvetica", 12, 'bold')

        self.create_widgets()



    def create_widgets(self):

        main_frame = tk.Frame(self.root, bg=self.bg_color)

        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_label = tk.Label(main_frame, text="Image Watermarking App", font=("Helvetica", 24, 'bold'), bg=self.bg_color, fg="#333333")

        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.upload_button = tk.Button(main_frame, text="Upload Image", command=self.upload_image, font=self.button_font, bg=self.button_color, fg="white", width=20, relief="flat")

        self.upload_button.grid(row=1, column=0, columnspan=3, pady=10)

        watermark_frame = tk.Frame(main_frame, bg=self.bg_color)

        watermark_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.watermark_text_label = tk.Label(watermark_frame, text="Enter Watermark Text:", font=("Helvetica", 12), bg=self.bg_color, fg=self.label_color)

        self.watermark_text_label.grid(row=0, column=0, padx=5)

        self.watermark_text_entry = tk.Entry(watermark_frame, font=("Helvetica", 12), width=30)

        self.watermark_text_entry.grid(row=0, column=1, padx=5)

        self.position_label = tk.Label(main_frame, text="Watermark Position:", font=("Helvetica", 12), bg=self.bg_color, fg=self.label_color)

        self.position_label.grid(row=3, column=0, pady=5, padx=5)

        self.position_var = tk.StringVar(value="Bottom Right")

        self.position_menu = tk.OptionMenu(main_frame, self.position_var, "Top Left", "Top Right", "Bottom Left", "Bottom Right")

        self.position_menu.config(font=("Helvetica", 12))

        self.position_menu.grid(row=3, column=1, pady=5, padx=5)

        self.opacity_label = tk.Label(main_frame, text="Watermark Opacity (0-255):", font=("Helvetica", 12), bg=self.bg_color, fg=self.label_color)

        self.opacity_label.grid(row=4, column=0, pady=5, padx=5)

        self.opacity_scale = tk.Scale(main_frame, from_=0, to=255, orient=tk.HORIZONTAL, font=("Helvetica", 12), bg=self.bg_color)

        self.opacity_scale.set(150)

        self.opacity_scale.grid(row=4, column=1, pady=10, padx=5)

        self.add_watermark_button = tk.Button(main_frame, text="Add Watermark", command=self.add_watermark, font=self.button_font, bg=self.button_color, fg="white", width=20, relief="flat")

        self.add_watermark_button.grid(row=5, column=0, columnspan=3, pady=10)

        self.save_button = tk.Button(main_frame, text="Save Image", command=self.save_image, font=self.button_font, bg="#FF5722", fg="white", width=20, relief="flat", state=tk.DISABLED)

        self.save_button.grid(row=6, column=0, columnspan=3, pady=10)

        self.quit_button = tk.Button(main_frame, text="Quit", command=self.root.quit, font=self.button_font, bg="#BDBDBD", fg="white", width=20, relief="flat")

        self.quit_button.grid(row=7, column=0, columnspan=3, pady=10)



    def upload_image(self):

        filetypes = (("JPEG files", "*.jpg;*.jpeg"), ("PNG files", "*.png"), ("All files", "*.*"))

        filepath = filedialog.askopenfilename(title="Select an Image", filetypes=filetypes)

        if filepath:

            self.filepath = filepath

            self.image = Image.open(filepath)

            max_size = (500, 500)

            self.image.thumbnail(max_size)

            self.watermarked_image = self.image.copy()

            self.save_button.config(state=tk.DISABLED)

            image_display = ImageTk.PhotoImage(self.image)

            if hasattr(self, 'image_label'):

                self.image_label.config(image=image_display)

            else:

                self.image_label = tk.Label(self.root, image=image_display)

                self.image_label.image = image_display

                self.image_label.pack(pady=10)



    def add_watermark(self):

        watermark_text = self.watermark_text_entry.get()

        if not watermark_text:

            messagebox.showerror("Error", "Please enter watermark text.")

            return

        opacity = self.opacity_scale.get()

        position = self.position_var.get()

        watermark = Image.new('RGBA', self.image.size, (0, 0, 0, 0))

        draw = ImageDraw.Draw(watermark, 'RGBA')

        try:

            font = ImageFont.truetype("arial.ttf", 40)

        except IOError:

            font = ImageFont.load_default()

        text_bbox = draw.textbbox((0, 0), watermark_text, font)

        text_width = text_bbox[2] - text_bbox[0]

        text_height = text_bbox[3] - text_bbox[1]

        x, y = self.get_position(position, text_width, text_height)

        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

        watermarked_image = Image.alpha_composite(self.image.convert('RGBA'), watermark)

        self.watermarked_image = watermarked_image.convert("RGB")

        self.image_label.config(image="")

        image_display = ImageTk.PhotoImage(watermarked_image)

        self.image_label = tk.Label(self.root, image=image_display)

        self.image_label.image = image_display

        self.image_label.pack(pady=10)

        self.save_button.config(state=tk.NORMAL)



    def get_position(self, position, text_width, text_height):

        if position == "Top Left":

            return 10, 10

        elif position == "Top Right":

            return self.image.width - text_width - 10, 10

        elif position == "Bottom Left":

            return 10, self.image.height - text_height - 10

        elif position == "Bottom Right":

            return self.image.width - text_width - 10, self.image.height - text_height - 10



    def save_image(self):

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])

        if save_path:

            self.watermarked_image.save(save_path)

            messagebox.showinfo("Success", "Watermarked image saved successfully.")



if __name__ == "__main__":

    root = tk.Tk()

    app = WatermarkApp(root)

    root.mainloop()

