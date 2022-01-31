from typing import Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from git import Repo
 


class GitInteract(App):

    def build(self):
        # self.window = GridLayout()
        # self.user = TextInput(multiline=False)
        # self.window.add_widget(self.user)
        #add widgets to windowwhichz
        gitButton = Button(text="ADD COMMIT PUSH")

        # gitButton
        return gitButton
    

    def git_push():

        try:
            repo = Repo(PATH_OF_GIT_REPO)
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