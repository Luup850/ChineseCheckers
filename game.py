import kivy
import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle, Color
import main as AI
import time

Builder.load_file('gui.kv')

class ChineseCheckersLayout(Widget):
    pass
    

class CheckersTable(GridLayout):
    
    selected = ObjectProperty(None, allownone=True)

    def press(self,position):
         
        # self.id_list = self.ids
        
        if self.selected == None:
            self.movefrom = position.name
            self.previous_color = position.color_testing
            self.selectPosition(position)
             
        else:
            self.moveto = position.name
            self.move(position)
            self.selected = None
            AImovefrom,AImoveto = AI.checkmovement(self.movefrom,self.moveto)
            print("------AI moves------",AImoveto)
            if AImoveto != "" :
                self.ids[AImoveto].color_testing = (20/255.0,199/255.0,0/255.0,1)
                self.ids[AImovefrom].color_testing = (177/255.0,179/255.0,181/255.0,1)

            
    def selectPosition(self, position):
        print(position.color_testing)
        if position.color_testing != [0.6941176470588235, 0.7019607843137254, 0.7098039215686275, 1]: 
            self.selected = position
            position.color_testing = (0,0,0,1)

        elif position.color_testing == [0.6941176470588235, 0.7019607843137254, 0.7098039215686275, 1]: 
            popup = Popup(
                    content=Label(text='Please remember to select a coloured piece to be moved'),
                    size_hint=(None, None),pos_hint={"x":0.5,"top":0.5} ,size=(40, 40))
            popup.open()
            
    def move(self,position):
        
        print("------Player moves-------",position.name)
        position.color_testing = self.previous_color
        self.selected.color_testing = (177/255.0,179/255.0,181/255.0,1)
        # self.ids.output_label.text = f'You selected:{position.name}'
        popup = Popup(title='Nice move!!',
                    content=Label(text='Now AI moves'),
                    size_hint=(0.2, 0.2),size=(400, 400))
        popup.open()
        
 

class gameApp(App):
    def build(self):
        Window.clearcolor = (138/255.0,98/255.0,56/255.0,1)
        
        return ChineseCheckersLayout()
     
#if __name__ == '__main__':
app = gameApp()
app.run()


# from kivy.uix.behaviors import ButtonBehavior
# from kivy.uix.image import Image
# from kivy.uix.button import Button
# from kivy.properties import NumericProperty, ReferenceListProperty
# from kivy.vector import Vector


# print(self.selected)
        #print(position.name)
#print(self.id_list)
        #print(self.ids)
        
        #self.ids.b0501.text = "X"
        #self.ids.b0501.color_testing = (177/255.0,179/255.0,181/255.0,1)
 #print(position.text)
            #print(self.selected.text)

 #print(dir(position))
        #print(position)
        #position.canvas.clear()
        
        #print(position.color_testing)

#position.background_color: rgba(177/255.0,79/255.0,96/255.0,1)
            #position.text = "X"

#validar el movimiento
        # print(self)
        # print(position)
#self.ids.b0501.text = "X"





# table = ObjectProperty(None)

    # print(f'TABLE: {table} ')
    
    # def reset(self):
    #     print(self.ids)
    #     # for position in self.table.ids:
        #     if self.table.ids[position] == ""
        #         self.table.ids[position].text = "O"
        #self.table.ids.b0012.text = 'tt'
        #self.table.ids.b0012.background_color = (0,0,1,1)
        #self.table.ids.b0111.text = 'X'
        #self.table.ids.b0113.text = 'X'
    #reset(table)

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
    # Print to the screen
        #     # self.add_widget(Label(text=f'Welcome you are going to be {players} players'))
            #print(f'Position selected: {self.selected}')
            
        #     # Clear the input boxes
        #     self.players.text = ""

# def reset(self):
    #     print(self.id_list)
    #     self.id_list.b0502.text = "X"

    #     # self.ids.color_testing = (177/255.0,179/255.0,181/255.0,1)
    #     #Green
    #     green = (20/255.0,199/255.0,0/255.0,1)
    #     self.id_list.b0012.color_testing = green
    #     self.ids.b0111.color_testing = green
    #     self.ids.b0113.color_testing = green
    #     self.ids.b0210.color_testing = green
    #     self.ids.b0212.color_testing = green
    #     self.ids.b0214.color_testing = green
    #     self.ids.b0309.color_testing = green
    #     self.ids.b0311.color_testing = green
    #     self.ids.b0313.color_testing = green
    #     self.ids.b0315.color_testing = green
    #     #Yellow
    #     #Orange
    #     #Red
        #Purple
        #Blue
