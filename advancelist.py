import os


folder=input("please provide a folder names with spaces:  ")

folder_list=folder.split(" ")

for folder in folder_list:
    file=os.listdir(folder)
    print(file)
    
    for file in file:
        print(file)
    


