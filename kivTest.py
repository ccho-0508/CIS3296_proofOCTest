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

class GitInteract(App):

    def build(self):
        # self.window = GridLayout()
        # self.user = TextInput(multiline=False)
        # self.window.add_widget(self.user)
        #add widgets to windowwhichz
        gitButton = Button(text="ADD COMMIT PUSH",
                    font_size ="15sp",
                   background_color =(1, 1, 1, 1),
                   color =(1, 1, 1, 1),
                   size =(32, 32),
                   size_hint =(.2, .2),
                   pos =(300, 250))
 
        gitButton.bind(on_press = self.git_push)

        # gitButton
        return gitButton
    
    @staticmethod
    def git_push(self):

        try:
            repo = Repo(PATH_GITREPO)
            repo.git.add(update=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push()
            print("Succesfully pushed changes to remote repo")
        except:
            print('Some error occured while pushing the code')   


    


GitInteract().run()





#     def on_text(instance, value):
#     print('The widget', instance, 'have:', value)

# textinput = TextInput()
# textinput.bind(text=on_text)