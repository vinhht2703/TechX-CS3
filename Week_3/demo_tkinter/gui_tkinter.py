import customtkinter

# custom theme & appearance
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")  # system, dark, light

# init UI
root = customtkinter.CTk()
root.title("Huynh Tan Vinh")
root.geometry("500x300")
root.resizable(0, 0)  # Don't allow resizing in the x or y direction

root.mainloop()
