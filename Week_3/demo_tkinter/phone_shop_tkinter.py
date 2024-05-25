import customtkinter
from PIL import Image
import json

phoneData = []
with open("data_phone.json", "r") as file:
    phoneData = json.load(file)


class Button(customtkinter.CTkButton):
    def __init__(
        self, master, text, pady, command, fg_color="blue", text_color="white"
    ):
        super().__init__(
            master=master,
            text=text,
            fg_color=fg_color,
            text_color=text_color,
            command=command,
        )
        self.pady = pady
        self.pack(pady=self.pady)


class Label(customtkinter.CTkLabel):
    def __init__(self, master, text, pady, image=None):
        super().__init__(master=master, text=text, pady=pady, image=image)
        self.pack()


class FramePhoneItem(customtkinter.CTkFrame):
    def __init__(self, master, row, column, imagePath, name, description, price, id):
        super().__init__(
            master=master,
            fg_color="black",
            border_color="green",
            border_width=1,
            corner_radius=15,
        )
        self.grid(row=row, column=column, sticky="news", padx=5, pady=5)
        self.imagePath = imagePath
        self.name = name
        self.description = description
        self.price = price
        self.id = id

        image = customtkinter.CTkImage(
            light_image=Image.open(self.imagePath),
            dark_image=Image.open(self.imagePath),
            size=(150, 150),
        )

        Label(self, text="", pady=80, image=image)
        Label(self, text=self.name, pady=0)
        Label(self, text=self.description, pady=10)
        Label(self, text=self.price, pady=10)
        Button(self, text="mua hàng", pady=10, command=lambda: self.onBuyItem())

    def onBuyItem(self):
        print(f"Selected phone id: {self.id}")


class FramePhoneList(customtkinter.CTkScrollableFrame):
    def __init__(self, master, data):
        super().__init__(master=master, fg_color="white")
        self.data = data
        self.pack(expand=True, fill="both")
        for index in range(0, 4):
            self.columnconfigure(index, weight=1)
            self.rowconfigure(index, weight=1)

        row = 0
        for pIdx in range(0, len(self.data)):
            phone = self.data[pIdx]

            if pIdx != 0 and pIdx % 4 == 0:
                row += 1
            FramePhoneItem(
                self,
                row,
                pIdx % 4,
                imagePath=phone["imagePath"],
                name=phone["name"],
                description=phone["description"],
                price=phone["price"],
                id=phone["id"],
            )


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Phone shop")
        self.geometry("900x720")

        FramePhoneList(self, data=phoneData)


app = App()

app.mainloop()
