import os

cwd = os.getcwd()
cwd +='\n/.git'

print(cwd)



fileo = open("testOpen.txt", "a")
fileo.write(cwd)

fileo.close()