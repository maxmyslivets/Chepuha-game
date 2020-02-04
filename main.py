# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder


with open("ChepuhaGameKV.kv", encoding='utf8') as f:
    drunk = f.read()


class ChepuhaGameApp(App):
    def build(self):
        Builder.load_string(drunk)


if __name__ == "__main__":
    ChepuhaGameApp().run()