from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextFieldRound


Builder.load_string("""
#:set color_shadow [0, 0, 0, .3]

<My_MDTextFieldRound>
    normal_color: color_shadow
    active_color: color_shadow

<Home>:

    scroll_for_players: scroll_for_players
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 20

        BoxLayout:
            My_MDTextFieldRound:
                text: '12345'
                size_hint_x: .5
        
        Scroll:
            id: scroll_for_players
            
        BoxLayout:
            size_hint_y: .2
            MDFillRoundFlatButton:
                text: 'add player'
                size_hint_x: .8
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: scroll_for_players.add()
""")


class My_MDTextFieldRound(MDTextFieldRound):
    
    pass


class Scroll(ScrollView):

    layoutForScroll = BoxLayout(
        orientation='vertical',
        spacing=10,
        size_hint_y=None)

    layoutForScroll.bind(minimum_height=layoutForScroll.setter('height'))

    playerNumber = [1, 2]


    def __init__(self, **kwargs):
        super(Scroll, self).__init__(**kwargs)

        for i in self.playerNumber:
            textFieldForPlayer = My_MDTextFieldRound(
            id = 'Player_'+str(i),
            hint_text = 'Player '+str(i),
            #pos_hint = {'center_x': .5},
            icon_left = 'face-recognition',
            icon_right = '')

            self.layoutForScroll.add_widget(textFieldForPlayer)
        
        self.add_widget(self.layoutForScroll)
    

    def add(self):

        self.playerNumber.append(self.playerNumber[-1]+1)

        textFieldForPlayer = My_MDTextFieldRound(
            id = 'Player_'+str(self.playerNumber[-1]),
            hint_text = 'Player '+str(self.playerNumber[-1]),
            #pos_hint = {'center_x': .5},
            icon_left = 'face-recognition',
            icon_right = '')

        self.layoutForScroll.add_widget(textFieldForPlayer)
        print(self.playerNumber)


class Home(Screen):

    pass


class MyApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))

        return sm


MyApp().run()
