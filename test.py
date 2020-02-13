from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


Builder.load_string("""#:include test.kv""")


from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line, Rectangle
from kivy.uix.button import Button

class CustomLayout(RelativeLayout):

    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)

        btn = Button(text='ghjk')

        self.add_widget(btn)


class Scroll(ScrollView):
    def __init__(self, **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(3):
            SkillStat = CustomLayout(pos=(0, 0), height=100, size_hint_y=None, size_hint_x=self.width)
            layout.add_widget(SkillStat)

        self.add_widget(layout)


class Home(Screen):

    def add_btn(self):
        Scroll().add_widget(Button(text='-=-=-=-=-=-=-=-'))


class MyApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))

        return sm


MyApp().run()

"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line, Rectangle
from kivy.uix.carousel import Carousel
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder


class CustomLayout(RelativeLayout):

    def __init__(self, **kwargs):
        super(CustomLayout, self).__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=(self.width, 90))
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class Scroll(ScrollView):
    def __init__(self, **kwargs):
        super(Scroll, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        # Make sure the height is such that there is something to scroll.
        for i in range(100):
            SkillStat = CustomLayout(pos=(0, 0), height=100, size_hint_y=None, size_hint_x=self.width)
            layout.add_widget(SkillStat)

        self.add_widget(layout)


class Sheet(Carousel):
    pass


Builder.load_file('test.kv')


class SheetApp(App):
    def build(self):
        return Sheet()


if __name__ == '__main__':
    SheetApp().run()
"""