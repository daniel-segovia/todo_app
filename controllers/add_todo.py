from csv import writer
import pandas as pd

def add_env(self):
    new_enviroment = input("insert new enviroment: \n")
    with open("model/enviroments.txt", "a") as ins_env:
        ins_env.write("\n" + new_enviroment)
        print(f"enviroment: {new_enviroment} added to list\n")
    self.update_view(id_env="-1")
        

