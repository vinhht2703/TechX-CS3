import customtkinter

# custom theme & appearance
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")  # system, dark, light

# init UI
root = customtkinter.CTk()
root.title("Demo Frame With Place")
root.geometry("900x720")

# frame
# arg1: master
frameTopLeft = customtkinter.CTkFrame(master=root, fg_color="yellow")
frameTopRight = customtkinter.CTkFrame(master=root, fg_color="red")
frameBotLeft = customtkinter.CTkFrame(master=root, fg_color="grey")
frameBotRight = customtkinter.CTkFrame(master=root, fg_color="blue")

## Place
### 0 - 1 => 0 -> 100%
frameTopLeft.place(relwidth=0.5, relheight=0.5, relx=0, rely=0)
frameTopRight.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0)
frameBotLeft.place(relwidth=0.5, relheight=0.5, relx=0, rely=0.5)
frameBotRight.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5)


# loop root screen for showing UI
root.mainloop()
