import os

cwd = os.getcwd()
cwd +='/selenium/chromedriver'

print(cwd)



fileo = open("testOpen.txt", "a")
fileo.write(cwd)

fileo.close()