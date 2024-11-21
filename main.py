import cv2
from tkinter import Tk, Button, Canvas, filedialog
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art")
        self.canvas = Canvas(root, width=500, height=500, bg="gray")
        self.canvas.pack()

        self.open_button = Button(root, text="Open Image", command=self.open_image)
        self.open_button.pack(pady=10)

        self.image = None

        self.root.bind("<Control-w>", self.close_app)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("JPG files", "*.jpg"),
                ("PNG fiels", "*.png"),
                ("WEBP files", "*.webp"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image(self.image)

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image.thumbnail((500, 500))
        self.tk_image = ImageTk.PhotoImage(image)

        self.canvas.create_image(250, 250, image=self.tk_image)

    def close_app(self, event=None):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ImageApp(root)
    root.mainloop()