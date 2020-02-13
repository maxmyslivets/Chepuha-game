from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


Builder.load_string("""#:include test.kv""")


class Home(Screen):

    pass


class MyApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))

        return sm


MyApp().run()