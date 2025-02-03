import random

names_random_number = []
names = []

def fileToList(filename):
    name_file = open(filename,"r")
    names = name_file.readlines()
    name_file.close()
    return names

def addRandomNumberToEnd(names):
    for name in names:
        name = name[:-1]+" "+str(random.randint(0,6))+"\n"
        names_random_number.append(name)
    return names_random_number
  
name_file = open("random.txt","w")
name_file.writelines(addRandomNumberToEnd(fileToList("names.txt")))
name_file.close()