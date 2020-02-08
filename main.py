from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window


Window.size = (300, 500)


Builder.load_string("""

# Icons for button
# New game 'restart'
# Next player 'skip-next'
# Exit 'logout' or 'close-circle' (-outline)
# The end 'presentation'
# start 'run'
# add player 'face-recognition' or 'creation'
# delete player 'close'


#:set color_shadow [0, 0, 0, .2980392156862745]


<MyTextInput@MDTextFieldRound>
    normal_color: color_shadow
    active_color: color_shadow


<Home>

    n_players: n_players

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'AppBackground_2.jpg'

    BoxLayout:
        orientation: 'vertical'

        MDIconButton:
            pos_hint: {'right': 1}
            icon: 'close'
            on_release: app.stop()

        BoxLayout:
            size_hint_y: .3

            Label:
                font_size: '40sp'
                text_size: self.size
                halign: 'center'
                valign: 'middle'
                text: 'Чепуха'
            
        BoxLayout:
            orientation: 'vertical'
            padding: 10
            spacing: 20
            
            MyTextInput:
                id: n_players
                size_hint_x: .9
                pos_hint: {'center_x': .5}
                icon_left: 'face-recognition'
                icon_right: ''
                hint_text: 'Player 1'
            
            MyTextInput:
                id: player_2
                size_hint_x: .9
                pos_hint: {'center_x': .5}
                icon_left: 'face-recognition'
                icon_right: ''
                hint_text: 'Player 2'

            BoxLayout:
                size_hint_y: .2
            
            MDFillRoundFlatButton:
                text: 'Старт'
                size_hint: .9, .1
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: root.first_game_screen(n_players.text)
                on_release: root.manager.current = 'NextGameScreen'
            
            BoxLayout:
                size_hint_y: .2


<NextGameScreen>:

    quests_data: quests_data
    answers_data: answers_data
    quests_label: quests_label

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'AppBackground_2.jpg'

    BoxLayout:
        orientation: 'vertical'

        AnchorLayout:
            size_hint_y: .5

            BoxLayout:

                FloatLayout:

                    MDFillRoundFlatButton:
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        size_hint_x: .8
                        text: 'Новая игра'

                        on_release: app.clear_var()
                        on_release: root.manager.current = 'Home'

                FloatLayout:

                    MDIconButton:
                        pos_hint: {'right': 1, 'top': 1}
                        valign: 'middle'
                        icon: 'close'

                        on_release: app.stop()

        Label:
            size_hint_y: .5
            id: quests_label
            text: 'Начните историю...'

        BoxLayout:
            orientation: 'vertical'
            padding: 20,0,20,0

            TextInput:
                id: answers_data
                hint_text: 'Введите ответ'

        BoxLayout:
            orientation: 'vertical'
            padding: 20,5,20,0

            TextInput:
                id: quests_data
                hint_text: 'Введите вопрос'
        
        FloatLayout:
            MDFillRoundFlatButton:
                pos_hint: {'center_x': .5, 'top': .9}
                # icon: 'skip-next'
                text: 'Передать ход'
                size_hint_y: .3
                on_release: root.add_data(answers_data.text, quests_data.text, quests_label.text)
        
        FloatLayout:
            MDFillRoundFlatButton:
                pos_hint: {'center_x': .5, 'center_y': .5}
                size_hint_x: .8
                text: 'Закончить'
                size_hint_y: .3
                on_release: root.end()
                on_release: root.manager.current = 'TheEndScreen'
                on_release: root.add_data(answers_data.text, quests_data.text, quests_label.text)
            

<TheEndScreen>:

    end_label: end_label

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'AppBackground_2.jpg'

    BoxLayout:
        orientation: 'vertical'

        FloatLayout:
            size_hint_y: .1

            MDIconButton:
                pos_hint: {'right': 1, 'top': 1}
                valign: 'middle'
                icon: 'close'

                on_release: app.stop()

        BoxLayout:
            padding: 20,20,20,20
            TextInput:
                id: end_label
        
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: .3

            FloatLayout:
                MDFillRoundFlatButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    text: 'Показать историю'
                    on_release: root.update_answers()
            
            FloatLayout:
                MDFillRoundFlatButton:
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    text: 'Сыграть ещё раз'
                    on_release: app.clear_var()
                    on_release: root.manager.current = 'Home'

""")


players, quests, answers, = [], [], []


class Home(Screen):

    def first_game_screen(self, numb_players):
        
        players = (numb_players.split(' '))
        print(players)


class NextGameScreen(Screen):

    quests_data = ObjectProperty()
    answers_data = ObjectProperty()
    quests_label = ObjectProperty()

    def add_data(self, add_answers, add_quests, quests_label):

        answers.append(add_answers)
        quests.append(add_quests)
        
        # XXX
        print(players)
        
        self.quests_label.text = '' + add_quests

        # FIXME
        #self.quests_label.text = players[0] + ', ' + add_quests
        #players.append(players[0])
        #players.remove(players[0])

        self.answers_data.text = ''
        self.quests_data.text = ''
    
    def end(self):

        TheEndScreen().update_answers()


class TheEndScreen(Screen):

    end_label = ObjectProperty()

    def update_answers(self):

        ans = ''
        for i in range(len(answers)):
            ans += answers[i] + '\n' + quests[i] + '\n'

        self.end_label.text = ans


class ChepuhaApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()
        sm.add_widget(Home(name='Home'))
        sm.add_widget(NextGameScreen(name='NextGameScreen'))
        sm.add_widget(TheEndScreen(name='TheEndScreen'))

        return sm
    
    def clear_var(self):
        pass
        #players, quests, answers, = [1, 2, 456], [], []


if __name__ == "__main__":

    ChepuhaApp().run()
