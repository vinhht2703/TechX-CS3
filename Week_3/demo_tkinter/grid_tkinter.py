import customtkinter

# custom theme & appearance
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")  # system, dark, light

# init UI
root = customtkinter.CTk()
root.title("Demo Frame With Grid")
root.geometry("900x720")

for index in range(0, 2):
    root.columnconfigure(index, weight=1)
    root.rowconfigure(index, weight=1)

# frame
frameTopLeft = customtkinter.CTkFrame(master=root, fg_color="yellow")
frameTopRight = customtkinter.CTkFrame(master=root, fg_color="red")
frameBotLeft = customtkinter.CTkFrame(master=root, fg_color="grey")
frameBotRight = customtkinter.CTkFrame(master=root, fg_color="blue")

## Grid
frameTopLeft.grid(row=0, column=0, sticky="news")
frameTopRight.grid(row=0, column=1, sticky="news")
frameBotLeft.grid(row=1, column=0, sticky="news")
frameBotRight.grid(row=1, column=1, sticky="news")


# loop root screen for showing UI
root.mainloop()
