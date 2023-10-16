from kivy.app import App
from kivy.uix.screenmanager import Screen



class PhotoEditorApp(App):
    pass

class Display(Screen):

    def display_image(self):
        return images[index]
    def user_image(self, user_input ):
        if user_input == "CatHalloween.jpg":
            self.ids.image.sources=self.display_image()

        self.ids.image.source= self.display_image()






PhotoEditorApp().run()