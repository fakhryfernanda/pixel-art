import cv2
from tkinter import Tk, Label, Frame, Button, Canvas, filedialog, Checkbutton, IntVar, Entry
from PIL import Image, ImageTk
from tkinter import Listbox

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Art Generator")

        self.initialize_widgets()

        self.image = None

        self.root.bind("<Control-w>", self.close_app)

    def initialize_widgets(self):
        # Create
        
        self.button_panel = Frame(root, height=500)
        self.top_button_frame = Frame(self.button_panel)
        self.bottom_button_frame = Frame(self.button_panel)
        
        self.open_button = Button(self.bottom_button_frame, text="Open Image", command=self.open_image)
        self.generate_button = Button(self.bottom_button_frame, text="Apply Settings", command=self.generate_image)
        self.canvas = Canvas(root, width=500, height=500, bg="gray")

        # Placement

        self.button_panel.grid(row=0, column=0, padx=20, pady=10, sticky="ns")
        self.top_button_frame.pack(side="top", anchor="nw")
        self.bottom_button_frame.pack(side="bottom")
        
        self.open_button.grid(row=0, column=0, padx=10, pady=10)
        self.generate_button.grid(row=0, column=1, padx=10, pady=10)
        self.canvas.grid(row=0, column=1)

    def initialize_image_control(self):
        self.is_pixelate = IntVar(value=0)
        self.pixelate_checkbox = Checkbutton(self.top_button_frame, text="Pixelate", variable=self.is_pixelate, command=self.toggle_pixelate)
        self.pixel_size_label = Label(self.top_button_frame, text="Pixel Size:")
        self.pixel_size = Entry(self.top_button_frame, width=3)

        self.is_quantize = IntVar(value=0)
        self.quantize_checkbox = Checkbutton(self.top_button_frame, text="Quantize", variable=self.is_quantize, command=self.toggle_quantize)
        self.quantize_label = Label(self.top_button_frame, text="Color Count:")
        self.quantize_color = Entry(self.top_button_frame, width=3)

        self.pixelate_checkbox.grid(row=0, column=0, sticky="NW")
        self.quantize_checkbox.grid(row=2, column=0, sticky="NW")
        
    def toggle_pixelate(self):
        if self.is_pixelate.get():
            self.pixel_size_label.grid(row=1, column=0, sticky="NW")
            self.pixel_size.grid(row=1, column=1, sticky="NW")
        else:
            self.pixel_size_label.grid_forget()
            self.pixel_size.grid_forget()

    def toggle_quantize(self):
        if self.is_quantize.get():
            self.quantize_label.grid(row=3, column=0, sticky="NW")
            self.quantize_color.grid(row=3, column=1, sticky="NW")
        else:
            self.quantize_label.grid_forget()
            self.quantize_color.grid_forget()

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
        
        self.initialize_image_control()
        self.show_dimension()

    def show_dimension(self):
        height, width, _ = self.image.shape
        self.dimension = Label(self.top_button_frame, text=f"Dimension: {width}x{height}")
        self.dimension.grid(row=4, column=0, columnspan=2)

    def generate_image():
        return
    
    def close_app(self, event=None):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ImageApp(root)
    root.mainloop()