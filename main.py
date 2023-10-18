import random

from PIL import Image, ImageDraw
from PIL.ImageDraw import ImageDraw
from kivy.app import App
from kivy.uix.screenmanager import Screen




class PhotoEditorApp(App):
    pass

class Display(Screen):

    def load_image(self):
        self.ids.image.source= self.ids.user_input.text

    def sepia( self, name):
        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                red1 = int(red * .393 + green * 0.769 + blue * 0.189)
                green1 = int(red * .349 + green * 0.686 + blue * 0.168)
                blue1 = int(red * .272 + green * 0.534 + blue * 0.131)
                pixels[x, y] = (red1, green1, blue1)
        img.save(name + "sepia.jpg")
        self.ids.image.source = name+ "sepia.jpg"


    def inverse(self,name):
        image =self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(name+ "invert.jpg")
        self.ids.image.source = name +"invert.jpg"




PhotoEditorApp().run()