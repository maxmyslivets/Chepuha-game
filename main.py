from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextFieldRound
from kivy.uix.boxlayout import BoxLayout


from kivy.core.window import Window
Window.size = (300, 500)


# FIXME: После сборки в .apk, возникает ошибка при попытке обращения к объекту аудиозаписи

sound = SoundLoader.load('media/wave.mp3')
sound.loop = True
#sound.play()

press_sound = SoundLoader.load('media/press.mp3')


class Home(Screen):

    Builder.load_string("""#:include kv/Home.kv""")
    

"""    def first_game_screen(self, player_1, player_2):
        
        ChepuhaApp().players.append(player_1)
        ChepuhaApp().players.append(player_2)

        NextGameScreen().start_quests_label()"""


class My_MDTextFieldRound(MDTextFieldRound):
    
    pass


# FIXME: Ширина TextField не подгоняется под ширину родителя


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
            icon_right = 'delete')
            #on_release = Scroll().removeTextField('self.id'))
            
            # FIXME: не тот способ присвоить действие нажатию

            self.layoutForScroll.add_widget(textFieldForPlayer)
        
        self.add_widget(self.layoutForScroll)
    

    def addTextFieldForNewPlayer(self):

        self.playerNumber.append(self.playerNumber[-1]+1)

        textFieldForPlayer = My_MDTextFieldRound(
            id = 'Player_'+str(self.playerNumber[-1]),
            hint_text = 'Player '+str(self.playerNumber[-1]),
            #pos_hint = {'center_x': .5},
            icon_left = 'face-recognition',
            icon_right = 'delete')

        self.layoutForScroll.add_widget(textFieldForPlayer)
        print(self.playerNumber)
    
    def removeTextField(self, widgetTextField):

        # FIXME: Как обратиться к полю ввода имени определенного игрока по его id и удалить его ??

        print(widgetTextField)
        #widgetTextField = ObjectProperty()
        #self.layoutForScroll.remove_widget(widgetTextField)



class NextGameScreen(Screen):

    Builder.load_string("""#:include kv/NextGameScreen.kv""")

    quests_data = ObjectProperty()
    answers_data = ObjectProperty()
    quests_label = ObjectProperty()

    def start_quests_label(self):

        # FIXME: Не добаляется имя игрока при первом появлении экрана

        self.quests_label.text = ChepuhaApp().players[-1] + ', начните историю...'

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
    
    Builder.load_string("""#:include kv/TheEndScreen.kv""")

    end_label = ObjectProperty()

    def update_answers(self):

        ans = ''
        for i in range(len(ChepuhaApp().answers)):
            ans += ChepuhaApp().answers[i] + '\n' + ChepuhaApp().quests[i] + '\n'

        self.end_label.text = ans


class ChepuhaApp(MDApp):

    players, quests, answers = ['name 1', 'name 2'], [], []

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

    def press_btn(self):

        # FIXME: При нажатии на любую кнопку должен появлятся звук нажатия, но он проигрывается только один раз.
        # При повторном нажатии звук не воспроизводится и ошибок приложения при этом не возникает.
        press_sound.play()
    
    def off_volume(self):

        if sound.volume: sound.volume = 0
        else: sound.volume = 1

        # FIXME: Не обновляется иконка громкости после нажатия на кнопку
        # self.volume_btn.icon = 'volume-high'


if __name__ == "__main__":

    ChepuhaApp().run()
