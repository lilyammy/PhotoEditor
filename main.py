import random

from PIL import Image, ImageDraw, ImageFilter
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget


class PhotoEditorApp(App):
    pass

class Display(Screen, Widget):
    coordinates = []
    # def on_touch_down(self,touch):
    #     x, y = touch.x, touch.y
    #     self.coordinates.append(int(x))
    #     self.coordinates.append(int(y))
    #     if len(self.coordinates)>6:
    #         self.coordinates= self.coodrinates[2:]
    #     print("Mouse pressed X:"+str(int(x)) + "y" + str(int(y)))
    #     touch.push()
    #     touch.apply_transform_2d(self.to_local)
    #     ret = super(RelativeLayout, self).on_touch_down(touch)
    #     touch.pop()
    #     return ret
    #
    # def on_touch_up(self, touch):
    #     x, y = touch.x, touch.y
    #     self.coordinates.append(int(x))
    #     self.coordinates.append(int(y))
    #     if len(self.coordinates) > 6:
    #         self.coordinates = self.coodrinates[2:]
    #     print("Mouse pressed X:" + str(int(x)) + "y" + str(int(y)))
    #     touch.push()
    #     touch.apply_transform_2d(self.to_local)
    #     ret = super(RelativeLayout, self).on_touch_up(touch)
    #     touch.pop()
    #     return ret

    def load_image(self):
        self.ids.image.source= self.ids.user_input.text

    def box2(self, x, y, width, height, red, blue, green):
        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        for yy in range(y, y + height):
            for xx in range(x, x + width):
                pixels[xx, yy] = (red, blue, green)
        self.ids.image.source = "box2.jpg"

    def pixelate(self, name):
        x= 370
        y=250
        width = 100
        height = 100
        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        red = 100
        blue = 100
        green = 100
        mod_factor_y = int(height / 5)
        mod_factor_x = int(width / 5)
        for yy in range(y, y + height):
            if yy % mod_factor_y == 0:
                for xx in range(x, x + width):
                    if xx % mod_factor_x == 0:
                        red = pixels[xx, yy][0]
                        green = pixels[xx, yy][1]
                        blue = pixels[xx, yy][2]
                        self.box2(self.ids.image.source, xx, yy, mod_factor_x, mod_factor_y, red, blue, green)

        img.save(name + "pixelate.jpg")
        self.ids.image.source = name + "pixelate.jpg"

    def line_drawing(self, name):

        image = self.ids.image.source
        img = Image.open(image)
        pixels = img.load()
        intensity = 10
        width = img.size[0]-1
        height = img.size[1]-1
        edge = img.filter(ImageFilter.FIND_EDGES)
        print(type(edge))

        draw = ImageDraw.Draw(edge)
        print(draw)
        for y in range(width):
            for x in range(height):
                pxl = edge.getpixel((x, y))
                if len(pxl) > intensity:
                    draw.point((x, y), fill="white")

        img.save(name + "line_drawing.jpg")
        self.ids.image.source = name + "line_drawing.jpg"


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