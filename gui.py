import kivy
from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        return Label(text="Hello World")

#if __name__ == '__name__':
myApp().run()