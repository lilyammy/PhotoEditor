import random

from PIL import Image, ImageDraw, ImageFilter
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from PIL import Image, ImageChops
import math


class PhotoEditorApp(App):
    pass

class Display(Screen, Widget):
    coordinates = []


    def load_image(self):
        self.ids.image.source= self.ids.user_input.text



    def sepia( self):
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
        img.save(image + "sepia.jpg")
        self.ids.image.source = image+ "sepia.jpg"

    def inverse(self):
        image =self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 255 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        img.save(image+ "invert.jpg")
        self.ids.image.source = image +"invert.jpg"

    def pointillism(self):
        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        random_int_list = []
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")
        for i in range(200000):
            size = random.randint(3, 13)
            x = random.randint(0, img.size[0] - size)
            y = random.randint(0, img.size[1] - size)
            red = pixels[x, y][0]
            green = pixels[x, y][1]
            blue = pixels[x, y][2]
            draw = ImageDraw.Draw(canvas)
            ellipsebox = [(x, y), (x + size, y + size)]
            draw.ellipse(ellipsebox, fill=(red, green, blue))
            del draw
        canvas.save(image + "pointillism.jpg")
        self.ids.image.source = image + "pointillism.jpg"


    def distance_halo(self):
        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        targetX = 300
        targetY = 350
        modifier = 2
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                distanceX = targetX - x
                distanceY = targetY - y
                distance = (distanceX * distanceX) + (distanceY * distanceY)
                distance_sqrt = math.sqrt(distance)
                quotient = int(distance_sqrt // modifier)
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]
                new_red = red - quotient
                new_green = green - quotient
                new_blue = blue - quotient
                if new_red < 0:
                    new_red = 0
                if new_green < 0:
                    new_green = 0
                if new_blue < 0:
                    new_blue = 0

                pixels[x, y] = (new_red, new_green, new_blue)
        img.save(image + "distance_halo.jpg")
        self.ids.image.source = image + "distance_halo.jpg"

    def lime_green(self):
        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        diff1 = -50
        diff2 = 145
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                pixels[x, y] = (pixels[x, y][0] - diff1, pixels[x, y][1] + diff2, pixels[x, y][2] + diff1)
        img.save(image + "lime_green.jpg")
        self.ids.image.source = image + "lime_green.jpg"



PhotoEditorApp().run()
