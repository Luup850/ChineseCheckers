import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# from kivy.properties import NumericProperty, ReferenceListProperty
# from kivy.vector import Vector

Builder.load_file('design.kv')

class ChineseCheckersLayout(Widget):
    
    players = ObjectProperty(None)

    def press(self):
        players = self.players.text

        # Print to the screen
        # self.add_widget(Label(text=f'Welcome you are going to be {players} players'))
        print(f'Welcome you are going to be {players} players')
        # Clear the input boxes
        self.players.text = ""


class gameApp(App):
    def build(self):
        return ChineseCheckersLayout()
     
#if __name__ == '__main__':
app = gameApp()
app.run()