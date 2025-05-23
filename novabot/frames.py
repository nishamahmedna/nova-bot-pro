from PIL import Image, ImageTk

def load_robot_image():
    image_path = "assets/novabot.png"
    image = Image.open(image_path).resize((400, 400), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)

