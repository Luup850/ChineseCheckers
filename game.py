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
import main as AI
import time

Builder.load_file('gui.kv')

class ChineseCheckersLayout(Widget):
    pass
    

class CheckersTable(GridLayout):
    
    selected = ObjectProperty(None, allownone=True)

    def press(self,position):
        
        if self.selected == None:
            self.movefrom = position.name
            self.previous_color = position.color_testing
            self.selectPosition(position)
             
        else:
            if position.color_testing == [0.6941176470588235, 0.7019607843137254, 0.7098039215686275, 1]:
                self.moveto = position.name
                self.move(position)
                self.selected = None
                AInumber, AImovefrom, AImoveto = AI.checkmovement(self.movefrom,self.moveto)
                print("------AI moves------",AImoveto)
                if AImoveto != "" :
                    colors = [(20/255.0,199/255.0,0/255.0,1), (252/255.0,233/255.0,3/255.0,1), (252/255.0,144/255.0,3/255.0,1), (20/255.0,199/255.0,0/255.0,1), (159/255.0,4/255.0,207/255.0,1), (0,0,1,1)]
                    for i,a in enumerate(AImoveto):
                        self.ids[a].color_testing = colors[AInumber[i]]
                    for i,a in enumerate(AImovefrom):
                        self.ids[a].color_testing = (177/255.0,179/255.0,181/255.0,1)

            elif position.color_testing != [0.6941176470588235, 0.7019607843137254, 0.7098039215686275, 1]:
                popup = Popup(title='Warning:',
                    content=Label(text='Ups! That gap is occupied by another peg, please select an empty space.'),
                    size_hint=(0.8, 0.2))
                popup.open()

            elif position.color_testing == [0,0,0,1]:
                popup = Popup(title='Warning:',
                    content=Label(text='Ups! You have already selected that peg. Remember that you must select the desire position.'),
                    size_hint=(0.8, 0.2))
                popup.open()
                
            
    def selectPosition(self, position):
        
        if position.color_testing != [0.6941176470588235, 0.7019607843137254, 0.7098039215686275, 1]: 
            self.selected = position
            position.color_testing = (0,0,0,1)

        elif position.color_testing == [0.6941176470588235, 0.7019607843137254, 0.7098039215686275, 1]: 
            popup = Popup(title='Warning:',
                    content=Label(text='Ups! That is an empty space, please select a red peg to be moved.'),
                    size_hint=(0.8, 0.2))
            popup.open()
            
    def move(self,position):
        
        print("------Player moves-------",position.name)
        position.color_testing = self.previous_color
        self.selected.color_testing = (177/255.0,179/255.0,181/255.0,1)
        popup = Popup(title='Nice move!!',
                    content=Label(text='Now AI moves'),
                    size_hint=(0.2, 0.2),size=(400, 400))
        #popup.open()
        
 

class gameApp(App):
    def build(self):
        Window.clearcolor = (138/255.0,98/255.0,56/255.0,1)
        
        return ChineseCheckersLayout()
     
## MAIN ##
app = gameApp()
app.run()