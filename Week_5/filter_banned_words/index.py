import customtkinter
from utils import hide_banned_words


class MessageContent(customtkinter.CTkLabel):
    def __init__(self, master, row, content):
        super().__init__(
            master=master,
            fg_color="green",
            text_color="white",
            text=content,
            corner_radius=10,
            justify="right",
            height=50,
        )
        self.row = row
        self.grid(
            row=self.row,
            column=1,
            sticky="e",
            pady=10,
            padx=2,
        )


class ChatInput(customtkinter.CTkEntry):
    def __init__(self, master):
        super().__init__(master=master)
        self.place(relwidth=0.8, relheight=0.6, relx=0.02, rely=0.2)


class ChatButton(customtkinter.CTkButton):
    def __init__(self, master, messageEntry, chatContentFrame):
        super().__init__(
            master=master,
            fg_color="green",
            text="Gửi",
            command=lambda: self.sendMessage(),
        )
        self.place(relwidth=0.1, relheight=0.4, relx=0.85, rely=0.3)
        self.messageEntry = messageEntry
        self.chatContentFrame = chatContentFrame

    def sendMessage(self):
        mess = self.messageEntry.get()
        if len(mess) > 0:
            censoredMess = hide_banned_words(mess)
            self.chatContentFrame.messageList.append(censoredMess)
            self.messageEntry.delete(0, "end")
            self.chatContentFrame.renderMessages()


class FrameChatBoxInput(customtkinter.CTkFrame):
    def __init__(self, master, chatContentFrame):
        super().__init__(
            master=master,
            fg_color="gray",
            corner_radius=0,
        )
        self.place(relwidth=1, relheight=0.2, relx=0, rely=0.801)
        messageEntry = ChatInput(self)
        ChatButton(self, messageEntry=messageEntry, chatContentFrame=chatContentFrame)


class FrameChatBoxContent(customtkinter.CTkScrollableFrame):
    def __init__(self, master, messageList):
        super().__init__(
            master=master,
            fg_color="gray",
            corner_radius=0,
        )
        self.messageList = messageList
        self.place(relwidth=1, relheight=0.8, relx=0, rely=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        for index in range(0, 3):
            self.rowconfigure(index, weight=1)

        self.renderMessages()

    def renderMessages(self):
        for widget in self.winfo_children():
            widget.destroy()

        for i in range(len(self.messageList)):
            mess = self.messageList[i]
            MessageContent(self, row=i, content=mess)


class FrameChatBoxWrapper(customtkinter.CTkFrame):
    def __init__(self, master, messageList):
        super().__init__(master=master, fg_color="white", corner_radius=0)
        self.pack(expand=True, fill="both")

        chatContentFrame = FrameChatBoxContent(self, messageList=messageList)
        FrameChatBoxInput(self, chatContentFrame=chatContentFrame)


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Chat box with filtering banned words")
        self.geometry("800x600")

        FrameChatBoxWrapper(self, messageList=["hahaha"])


app = App()
app.mainloop()
