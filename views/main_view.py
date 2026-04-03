from model import todoData
from model import list_tasks_frames
from controllers import add_todo
from controllers import remove_todo
from controllers import add_task
from controllers import print_tasks
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
        self.dd.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=5)
        self.dd.configure(state="readonly")

        self.scroll_frame = list_tasks_frames.ScrollableFrame(
            self.app,
            width=300,
            height=150
        )
        self.scroll_frame.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
        
        # Textarea (Row 1)

        # Buttons (Row 2)
        self.btn = ctk.CTkButton(
            self.app,
            text="new env",
            command=self.add_enviroment
        )
        self.btn.grid(row=2, column=0, sticky="ew", padx=7, pady=5)

        self.addtsk = ctk.CTkButton(
            self.app,
            text="add task",
            command=self.add_task
        )
        self.addtsk.grid(row=2, column=1, sticky="ew", padx=7, pady=5)

        self.removetsk = ctk.CTkButton(
            self.app,
            text="remove selected enviroment",
            command=self.remove_env
        )
        self.removetsk.grid(row=2, column=2, sticky="ew", padx=7, pady=5)

        # Make rows/columns expand nicely
        self.app.grid_rowconfigure(1, weight=1)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_columnconfigure(1, weight=1)
        self.app.grid_columnconfigure(2, weight=1)

        add_todo.update_view(self)
        self.print_tasks_func()
        

    def runApp(self):
        self.app.mainloop()

    def add_enviroment(self):
        add_todo.add_env(self)

    def add_task(self):
        dialog = add_task.TaskDialog(self)
        if dialog.value:
            title, desc = dialog.value
            # ejemplo: escribir en el combo

    def remove_env(self):
        remove_todo.remove_env(self)

    def print_tasks_func(self):
        env = self.dd.get()
        self.scroll_frame.update_dd(env)
        self.scroll_frame.print_tasks_list(env)
        #list_tasks_frames.print_tasks_list(self, env)
