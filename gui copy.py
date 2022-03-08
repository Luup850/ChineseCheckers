import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# from kivy.properties import NumericProperty, ReferenceListProperty
# from kivy.vector import Vector


class chineseCheckersGame(Widget):
    pass


# KV = """
# FLoatLayout:
#     BoxLayout:
#         id: checkers_board
#         orientation "vertical"
# """

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self,**kwargs):
        # Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        # Set the columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 400

        # Create a second gridlayout. Set the height and width of the columns
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=400
            )
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Number of players: "))
            # size_hint_y = None,
            # height = 50,
            # size_hint_x = None,
            # width = 400))
        # Add Input Box with only 1 line
        self.players = TextInput(multiline=False)
            # size_hint_y = None,
            # height = 50,
            # size_hint_x = None,
            # width = 400)
        self.top_grid.add_widget(self.players)

        # Add the new top grid to our app
        self.add_widget(self.top_grid)


        # Create a Submit Button
        self.submit = Button(text="Submit", 
            font_size=32,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width = 200
            )
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        players = self.players.text

        # Print to the screen
        self.add_widget(Label(text=f'Welcome you are going to be {players} players'))

        # Clear the input boxes
        self.players.text = ""


class chineseCheckersApp(App):
    def build(self):
        #return Label(text="Hello World",font_size=72)
        return MyGridLayout()
        #Window.size = [800,800]
        #return Builder.load_string(KV)
        #return chineseCheckersGame()

    # def on_start(self):
    #     board = self.root.ids.checkers_board
    #     for i in range (24):
    #         board_row = BoxLayout(orientation="horizontal")
    #         for j in range(16):
    #             board_row.add_widget(Button(background_normal= "",
    #                 background_color = [1,1,1,1]))
    #         board.add_widget(board_row)


#if __name__ == '__main__':
app = chineseCheckersApp()
app.run()