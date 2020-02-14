from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextFieldRound
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton

class CastomMDTextFieldRound(MDTextFieldRound):

    icon_right = ''

    def __init__(self, **kwargs):
        super(CastomMDTextFieldRound, self).__init__(**kwargs)

        btn = MDIconButton(
            icon='delete', 
            pos_hint={'right': 1})
        btn.bind(on_press= lambda x:Home().func())

        layout = FloatLayout()
        layout.add_widget(btn)

        self.add_widget(layout)


class Home(BoxLayout):
    
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

        self.add_widget(CastomMDTextFieldRound())
    
    def func(self):
        print('test -- ok!')


class MyApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        return Home()


MyApp().run()
