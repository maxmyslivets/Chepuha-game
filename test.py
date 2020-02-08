from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string('''

<testclass>:
    padding: 20,0,0,0

    FloatLayout:
        MDFillRoundFlatButton:
            size_hint_x: .5
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: 'New Game'
        
    FloatLayout:
        MDIconButton:
            pos_hint: {'right': 1, 'center_y': .5}
            icon: 'close'

''')

class testclass(BoxLayout):
    pass

class Example(MDApp):

    def build(self):
        return testclass()


Example().run()