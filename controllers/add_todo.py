from tkinter import messagebox, simpledialog

#create new enviroment
def add_env(self):
    #new_enviroment = input("insert new enviroment: \n")
    new_enviroment = simpledialog.askstring("title","insert new enviroment: \n")
    with open("model/enviroments.txt", "a") as ins_env:
        if not new_enviroment:
            alert = ValueError("Enviroment cannot be empty")
            print(alert)
            return
        else:
            ins_env.write("\n" + new_enviroment)
            print(f"enviroment: {new_enviroment} added to list\n")
            
            with open(f"model/files/{new_enviroment}.csv", "w") as new_file:
                new_file.write("-----start-----")
    update_view(self, id_env="-1")
    

        
#populate dropdown with available enviroments
def update_view(self, env_file="model/enviroments.txt", id_env=0):
    with open(env_file, "r") as env_file:
        self.enviroments = []
        self.enviroments = [line.strip() for line in env_file if line.strip()]
        print(self.enviroments)

    self.dd.configure(values=self.enviroments)
    self.dd.update_idletasks()

    if self.enviroments:
        self.dd.set(self.enviroments[int(id_env)])
