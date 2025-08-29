import tkinter as tk
import os
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "src", "icon.png")
        master.iconphoto(False, tk.PhotoImage(file=icon_path))
        master.minsize(700, 700)

        window_width = 700
        window_height = 700
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        master.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        master.config(bg="#9DDB18")

        font = ("Arial", 14)

        self.text_label = tk.Label(master, text="Enter text:", font=font, bg="#DBBB07", fg="#ffffff")
        self.text_label.pack(pady=(10, 0))

        self.text_area = tk.Text(master, height=5, font=font, bg="#DBD507", fg="black")
        self.text_area.pack(pady=5, padx=20, fill='x')

        self.button_frame = tk.Frame(master, bg="#9DDB18")
        self.button_frame.pack(pady=5)

        self.generate_button = tk.Button(self.button_frame, text="Generate", command=self.generate_qr_code, font=font, bg="#0BDB25", fg="#ffffff")
        self.generate_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_text_and_qr, font=font, bg="#0BDB25", fg="#ffffff")
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.qr_code_label = tk.Label(master, bg="#9DDB18")
        self.qr_code_label.pack(pady=10, padx=20, expand=True, fill='both')

        self.download_button = tk.Button(master, text="Download", command=self.download_qr_code, state=tk.DISABLED, font=font, bg="#0BDB25", fg="#ffffff")
        self.download_button.pack(pady=(0, 10))

        self.qr_code_image = None

    def generate_qr_code(self):
        text = self.text_area.get("1.0", "end-1c")
        if text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text)
            qr.make(fit=True)

            self.qr_code_image = qr.make_image(fill_color="black", back_color="white")

            # Convert PIL image to Tkinter image
            img = self.qr_code_image.resize((400, 400))
            self.tk_image = ImageTk.PhotoImage(img)

            self.qr_code_label.config(image=self.tk_image)
            self.download_button.config(state=tk.NORMAL)

    def download_qr_code(self):
        if self.qr_code_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.qr_code_image.save(file_path)

    def clear_text_and_qr(self):
        self.text_area.delete("1.0", "end")
        self.qr_code_label.config(image='')
        self.qr_code_label.image = None
        self.download_button.config(state=tk.DISABLED)
        self.qr_code_image = None

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()
