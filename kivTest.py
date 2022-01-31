# https://stackoverflow.com/questions/41836988/git-push-via-gitpython/54111480

from cgitb import text
from typing import Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from git import Repo

import os 


PATH_GITREPO = os.getcwd()
PATH_GITREPO +='/.git'
COMMIT_MESSAGE = "Test GUI"

fo = open("test.txt", "w")


class GitInteract(App):

    def build(self):
        self.window = GridLayout()
        # self.user = TextInput(multiline=False)
        # self.window.add_widget(self.user)
        #add widgets to windowwhichz
        gitButtonPush = Button(text="Push to Repo",
                    font_size ="15sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(300,150),
                   pos =(450, 250))

        gitButtonPull = Button(text= "Pull from Repo",
                    font_size = "15sp",
                   background_color = (1, 1, 1, 1),
                   color = (1, 1, 1, 1),
                   size = (300,150),
                   pos = (800, 250))

        textinput = TextInput(text='',
                    size =(300,150),
                    pos = (625, 50))

        self.window.add_widget(textinput)
        textinput.bind(text = self.updateFile)
    
        gitButtonPush.bind(on_press = self.git_push)
        gitButtonPull.bind(on_press = self.git_pull)

        self.window.add_widget(gitButtonPush)
        self.window.add_widget(gitButtonPull)
       
        return self.window
    
    def updateFile(self, instance, text):
        print(text)
        fo.write(text+"\n")
        

    @staticmethod

    def git_push(self):
        fo.flush()
        os.fsync(fo.fileno())
        try:
            repo = Repo(PATH_GITREPO)
            repo.git.add(all=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push()
            print("Succesfully pushed changes to remote repo")    
            

        except:
            print('Some error occured while pushing the code')   
        
    

    @staticmethod
    def git_pull(self):
        try:
            repo = Repo(PATH_GITREPO)
            origin = repo.remote(name='origin')
            origin.pull()
            print("Succesfully pulled changes from remote repo")
        except:
            print('Some error occured while pulling the code')   
    




    
if __name__ == "__main__":
    GitInteract().run()





#     def on_text(instance, value):
#     print('The widget', instance, 'have:', value)

# textinput = TextInput()
# textinput.bind(text=on_text)