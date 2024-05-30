import customtkinter
from utils import auto_complete_search
from data import rawData


class HeaderTitle(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(
            master=master,
            text="Dictionary",
            text_color="black",
            justify="center",
            font=("", 30),
        )
        self.grid(row=0, column=0, sticky="news", pady=10, padx=10)


class TranslationContent(customtkinter.CTkLabel):
    def __init__(self, master):
        super().__init__(
            master=master,
            text="",
            text_color="black",
            anchor="nw",
            font=("", 25),
            padx=30,
            pady=30,
        )
        self.place(relwidth=0.99, relheight=1, relx=0.03, rely=0.03)

    def update_text(self, text):
        self.configure(text=text)


class WordLabel(customtkinter.CTkButton):
    def __init__(self, master, row, word, translation_content):
        super().__init__(
            master=master,
            text=word,
            hover_color="grey",
            anchor="w",
            fg_color="black",
            text_color="white",
            font=("", 20),
            command=self.on_translate,
        )
        self.word = word
        self.row = row
        self.translation_content = translation_content
        self.grid(row=self.row, column=0, sticky="news", pady=5, padx=10)

    def on_translate(self):
        translation = rawData[self.word]
        text = f"{self.word} ({translation['part_of_speech']}): {translation['vn']}"
        self.translation_content.update_text(text)


class FrameWordList(customtkinter.CTkScrollableFrame):
    def __init__(self, master, translation_content):
        super().__init__(master=master, fg_color="black", corner_radius=0)
        self.grid(row=1, column=0, sticky="news", padx=10)
        self.columnconfigure(0, weight=1)

        row = 0
        for word in rawData.keys():
            self.rowconfigure(row, weight=1)
            WordLabel(self, row=row, word=word, translation_content=translation_content)
            row += 1


class FrameLeft(customtkinter.CTkFrame):
    def __init__(self, master, translation_content):
        super().__init__(master=master, fg_color="grey", corner_radius=0)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=9)
        self.columnconfigure(0, weight=1)

        HeaderTitle(self)
        FrameWordList(self, translation_content)


class AutoCompleteInput(customtkinter.CTkEntry):
    def __init__(self, master):
        super().__init__(
            master=master, fg_color="silver", text_color="black", font=("", 20)
        )
        self.pack(expand=True, fill="both")

        self.bind("<KeyRelease>", lambda event: master.onSearchWords(event, self.get()))


class FrameAutoCompleteInput(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="silver", corner_radius=0)
        self.grid(row=0, column=0, sticky="news", padx=10, pady=10)

        AutoCompleteInput(self)

    def onSearchWords(self, event, searchKey):
        self.master.translation_frame.translation_content.update_text("")
        self.master.autoCompleteResultFrame.renderResult(searchKey)


class FrameAutoCompleteResult(customtkinter.CTkScrollableFrame):
    def __init__(self, master, translation_content):
        super().__init__(master=master, fg_color="black", corner_radius=0)
        self.grid(row=1, column=0, sticky="news", padx=10)
        self.columnconfigure(0, weight=1)
        self.searchKey = ""
        self.translation_content = translation_content
        self.renderResult()

    def renderResult(self, searchKey=""):
        foundWords = auto_complete_search(searchKey)
        for widget in self.winfo_children():
            widget.destroy()

        if searchKey is None or searchKey == "":
            return

        row = 0
        for word in foundWords:
            self.rowconfigure(row, weight=1)
            WordLabel(
                self, row=row, word=word, translation_content=self.translation_content
            )
            row += 1


class FrameTranslation(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="silver", corner_radius=0)
        self.grid(row=2, column=0, sticky="news")

        self.translation_content = TranslationContent(self)


class FrameRight(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="silver", corner_radius=0)
        self.grid(row=0, column=1, sticky="news")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=7)

        FrameAutoCompleteInput(self)
        self.translation_frame = FrameTranslation(self)
        self.autoCompleteResultFrame = FrameAutoCompleteResult(
            self, self.translation_frame.translation_content
        )


class FrameDictionary(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="white", corner_radius=0)
        self.pack(expand=True, fill="both")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=3)

        translation_frame = FrameRight(self).translation_frame
        FrameLeft(self, translation_content=translation_frame.translation_content)


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Dictionary")
        self.geometry("800x600")

        FrameDictionary(self)


app = App()
app.mainloop()
