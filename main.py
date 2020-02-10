from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader


from kivy.core.window import Window
Window.size = (300, 500)


sound = SoundLoader.load('media/wave.mp3')
sound.loop = True
sound.play()


class Home(Screen):

    with open("kv/Home.kv", encoding='utf8') as HomeKV:
        Builder.load_string(HomeKV.read())

    def first_game_screen(self, player_1, player_2):
        
        ChepuhaApp().players.append(player_1)
        ChepuhaApp().players.append(player_2)

        NextGameScreen().start_quests_label()


class NextGameScreen(Screen):

    with open("kv/NextGameScreen.kv", encoding='utf8') as NextGameScreenKV:
        Builder.load_string(NextGameScreenKV.read())

    quests_data = ObjectProperty()
    answers_data = ObjectProperty()
    quests_label = ObjectProperty()

    def start_quests_label(self):
        self.quests_label.text = ChepuhaApp().players[1] + ', начните историю...'

    def add_data(self, add_answers, add_quests, quests_label):

        ChepuhaApp().answers.append(add_answers)
        ChepuhaApp().quests.append(add_quests)

        self.quests_label.text = ChepuhaApp().players[0] + ', ' + add_quests
        ChepuhaApp().players.append(ChepuhaApp().players[0])
        ChepuhaApp().players.remove(ChepuhaApp().players[0])

        self.answers_data.text = ''
        self.quests_data.text = ''
    
    def end(self):

        TheEndScreen().update_answers()


class TheEndScreen(Screen):

    with open("kv/TheEndScreen.kv", encoding='utf8') as TheEndScreenKV:
        Builder.load_string(TheEndScreenKV.read())

    end_label = ObjectProperty()

    def update_answers(self):

        ans = ''
        for i in range(len(ChepuhaApp().answers)):
            ans += ChepuhaApp().answers[i] + '\n' + ChepuhaApp().quests[i] + '\n'

        self.end_label.text = ans


class ChepuhaApp(MDApp):

    players, quests, answers = [], [], []

    def build(self):

        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))
        sm.add_widget(NextGameScreen(name='NextGameScreen'))
        sm.add_widget(TheEndScreen(name='TheEndScreen'))

        return sm
    
    def clear_var(self):
        
        self.players.clear()
        self.quests.clear()
        self.answers.clear()
    
    volume_btn = ObjectProperty()
    
    def off_volume(self):

        if sound.volume: sound.volume = 0
        else: sound.volume = 1

        #self.volume_btn.icon = 'volume-high'


if __name__ == "__main__":

    ChepuhaApp().run()
