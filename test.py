from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


Builder.load_string("""

<Home>:

    input_1: input_1

    BoxLayout:
        TextInput:
            id: input_1
        Button:
            text: 'Next screen'
            on_release: root.label_update(input_1.text)
            on_release: root.manager.current = 'NextScreen'


<NextScreen>:

    label_1: label_1

    BoxLayout:
        Label:
            id: label_1
            text: 'qwerty'
        Button:
            text: 'The End screen'
            on_release: root.manager.current = 'TheEndScreen'


<TheEndScreen>:

    Button:
        text: 'Home'
        on_release: app.clear_input()
        on_release: root.manager.current = 'Home'

""")


class Home(Screen):

    input_1 = ObjectProperty()
    
    def label_update(self, input_1):

        NextScreen().label_1.text = input_1


class NextScreen(Screen):
    
    label_1 = ObjectProperty(rebind=True)


class TheEndScreen(Screen):
    pass


class MyApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))
        sm.add_widget(NextScreen(name='NextScreen'))
        sm.add_widget(TheEndScreen(name='TheEndScreen'))

        return sm
    
    def clear_input(self):

        Home().input_1.text = ''



MyApp().run()