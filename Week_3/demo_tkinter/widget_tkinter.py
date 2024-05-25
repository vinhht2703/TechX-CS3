import customtkinter

# custom theme & appearance
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")  # system, dark, light

# init UI
root = customtkinter.CTk()
root.title("Huynh Tan Vinh")
root.geometry("900x720")


def button_event():
    print(entry.get())


entry = customtkinter.CTkEntry(root, placeholder_text="Enter something")
button = customtkinter.CTkButton(
    root,
    text="Press btn",
    fg_color="blue",
    text_color="white",
    command=lambda: button_event(),
)

entry.pack()
button.pack()

# pip3 install Pillow
from PIL import Image

image_link = "./img/penguin.png"
my_image = customtkinter.CTkImage(
    light_image=Image.open(image_link),
    dark_image=Image.open(image_link),
    size=(300, 300),
)

image_label = customtkinter.CTkLabel(
    root, image=my_image, text=""
)  # display image with a CTkLabel

image_label.pack()


root.mainloop()
