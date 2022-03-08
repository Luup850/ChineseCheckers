import kivy
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.behaviors import ButtonBehavior
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.properties import NumericProperty, ReferenceListProperty
# from kivy.vector import Vector

Builder.load_file('gui.kv')
directory = os.getcwd()

# class BoubleButton(ButtonBehavior, Image):
#     def __init__(self, **kwargs):
#         super(BoubleButton, self).__init__(**kwargs)
#         self.source = directory+'bouble.png'

    # def on_press(self):
    #     self.source = 'atlas://data/images/defaulttheme/checkbox_on'

    # def on_release(self):
    #     self.source = 'atlas://data/images/defaulttheme/checkbox_off'
# class BoubleButton(Button):
#     pass

class ChineseCheckersLayout(Widget):
    selected = ObjectProperty(None, allownone=True)
    table = ObjectProperty(None)

    def press(self,position):

        print(position.text)

        if self.selected == None:
            self.selectPosition(position)
            print(position.text)
            print(self.selected.text)

        else:
            if self.selected != None:
                #self.move(position)
                self.selected = None
            else:
                self.selected.text = ""
                self.selected = None


        # Print to the screen
    #     # self.add_widget(Label(text=f'Welcome you are going to be {players} players'))
        #print(f'Position selected: {self.selected}')
        
    #     # Clear the input boxes
    #     self.players.text = ""

    def selectPosition(self, position):
        if position.text == "":
            self.selected = position
            position.text = "X"

    # def reset(self):
    #         for position in self.table.ids:
    #             if self.table.ids[position] == ""
    #                 self.table.ids[position].text = "O"
    #         self.table.ids.cr3c3.text = ''


class gameApp(App):
    def build(self):
        Window.clearcolor = (138/255.0,98/255.0,56/255.0,1)
        return ChineseCheckersLayout()
     
#if __name__ == '__main__':
app = gameApp()
app.run()