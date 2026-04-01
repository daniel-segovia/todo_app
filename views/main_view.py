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
        self.addtsk = ctk.CTkButton(
            self.app, width=100, height=20,
            text = "add task",
            command = self.add_task
        )
        self.dd.pack(pady=10)
        self.addtsk.pack(pady=10)

        add_todo.update_view(self)
        
    def runApp(self):
        self.app.mainloop()

    def add_enviroment(self):
        add_todo.add_env(self)

    def add_task(self):
        add_todo.add_task(self)
 
