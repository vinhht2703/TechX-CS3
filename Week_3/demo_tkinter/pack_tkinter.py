import customtkinter

# custom theme & appearance
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")  # system, dark, light

# init UI
root = customtkinter.CTk()
root.title("Demo Tkinter")
root.geometry("900x720")

# frame
# arg1: master
# frame = customtkinter.CTkFrame(master=root, fg_color="red", width=100, height=50)
frameLeft = customtkinter.CTkFrame(master=root, fg_color="white")
frameRight = customtkinter.CTkFrame(master=root, fg_color="white")
frameLeftTop = customtkinter.CTkFrame(master=frameLeft, fg_color="yellow")
frameLeftBot = customtkinter.CTkFrame(master=frameLeft, fg_color="gray")
frameRightTop = customtkinter.CTkFrame(master=frameRight, fg_color="red")
frameRightBot = customtkinter.CTkFrame(master=frameRight, fg_color="blue")

## pack
### side = top, bottom, left, right
### expand = True, False
### fill = both, x, y
frameLeft.pack(side="left", expand=True, fill="both")
frameRight.pack(side="right", expand=True, fill="both")
frameLeftTop.pack(side="top", expand=True, fill="both")
frameLeftBot.pack(side="bottom", expand=True, fill="both")
frameRightTop.pack(side="top", expand=True, fill="both")
frameRightBot.pack(side="bottom", expand=True, fill="both")

# loop root screen for showing UI
root.mainloop()
