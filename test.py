from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextFieldRound
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button

class CastomMDTextFieldRound(MDTextFieldRound):

    icon_right = ''
    size_hint = (.5, None)

    def __init__(self, **kwargs):
        super(CastomMDTextFieldRound, self).__init__(**kwargs)

        btn = MDIconButton(
            icon='delete', 
            pos_hint={'right': 1})
            
        btn.bind(on_release = lambda x: Home().func())

        

        layout = FloatLayout(size_hint=(1,1))
        layout.add_widget(btn)

        self.add_widget(layout)


class Home(BoxLayout):
    
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

        layoutbox = FloatLayout()
        layoutbox.add_widget(MDTextFieldRound(pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.5, None)))
        self.add_widget(layoutbox)
    
    def func(self):
        print('test -- ok!')


class MyApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        return Home()


MyApp().run()
