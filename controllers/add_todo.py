from csv import writer
import pandas as pd


#create new enviroment
def add_env(self):
    new_enviroment = input("insert new enviroment: \n")
    with open("model/enviroments.txt", "a") as ins_env:
        ins_env.write("\n" + new_enviroment)
        print(f"enviroment: {new_enviroment} added to list\n")
    update_view(self, id_env="-1")
    with open(f"model/{new_enviroment}.csv", "w") as new_file:
        new_file.write("user,title,description,status")
        
#populate dropdown with available enviroments
def update_view(self, env_file="model/enviroments.txt", id_env=0):
    with open(env_file, "r") as env_file:
        self.enviroments = []
        self.enviroments = [line.strip() for line in env_file if line.strip()]

    self.dd.configure(values=self.enviroments)
    if self.enviroments:
        self.dd.set(self.enviroments[int(id_env)])

def add_task(self):
    env = self.dd.get()
    with open(f"{env}.csv", "r") as env_test:
        print(env_test.read())



