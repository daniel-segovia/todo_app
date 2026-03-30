from model import todoData
from controllers import add_todo
import customtkinter as ctk

class todoView:

    def __init__(self, todoList=""):
        self.enviroments = []

        self.app = ctk.CTk()

        self.app.title("test")
        self.app.geometry("400x400")

        self.btn = ctk.CTkButton(
            self.app,
            text = "new env",
            command  = self.add_enviroment
        )
        self.btn.pack(pady=10)

        self.dd = ctk.CTkComboBox(
            self.app, width=300, height=100
        )
        self.dd.pack(pady=10)

        self.update_view()

    def update_view(self, env_file="model/enviroments.txt", id_env=1):
        with open(env_file, "r") as env_file:
            self.enviroments = []
            self.enviroments = [line.strip() for line in env_file]

        self.dd.configure(values=self.enviroments)
        if self.enviroments:
            self.dd.set(self.enviroments[int(id_env)])
        
    def runApp(self):
        self.app.mainloop()

    def add_enviroment(self):
        add_todo.add_env(self)
 
