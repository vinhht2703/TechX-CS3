import customtkinter


class FrameGrid(customtkinter.CTkScrollableFrame):
    def __init__(self, master, fg_color):
        super().__init__(master=master, fg_color=fg_color)
        self.grid(row=0, column=0, sticky="news")

        for i in range(100):
            button = customtkinter.CTkButton(
                self,
                text=f"Button {i} !",
                fg_color="green",
                text_color="white",
                command=lambda idx=i: self.button_event(idx),
            )
            button.pack(pady=10)

    def button_event(self, curIndex):
        print(f"Current index: {curIndex}")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Class with Tkinter")
        self.geometry("900x720")

        FrameGrid(self, "gray")


app = App()

app.mainloop()
