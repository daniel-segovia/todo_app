from model import todoData
from controllers import add_todo
import customtkinter as ctk

class todoView:

    def __init__(self, todoList=""):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.enviroments = []

        self.app = ctk.CTk()
        self.app.title("test")
        self.app.geometry("400x400")

        # Dropdown (Row 0)
        self.dd = ctk.CTkComboBox(
            self.app, width=150, height=30
        )
        self.dd.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Textarea (Row 1)
        self.text_area = ctk.CTkTextbox(
            self.app,
            width=300,
            height=150,
            scrollbar_button_color="black",
            activate_scrollbars=True
        )
        self.text_area.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        self.text_area.configure(state="disabled")

        # Buttons (Row 2)
        self.btn = ctk.CTkButton(
            self.app,
            text="new env",
            command=self.add_enviroment
        )
        self.btn.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        self.addtsk = ctk.CTkButton(
            self.app,
            text="add task",
            command=self.add_task
        )
        self.addtsk.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

        # Make rows/columns expand nicely
        self.app.grid_rowconfigure(1, weight=1)   # Textarea expands
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)

        add_todo.update_view(self)

    def runApp(self):
        self.app.mainloop()

    def add_enviroment(self):
        add_todo.add_env(self)

    def add_task(self):
        add_todo.add_task(self)
