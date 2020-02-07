from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


Builder.load_string("""

<Home>

    n_players: n_players

    BoxLayout:
        orientation: 'vertical'
        padding: 50

        Label:
            font_size: '40sp'
            text_size: self.size
            halign: 'center'
            valign: 'top'
            text: 'Chepuha'
        
        TextInput:
            id: n_players
            text: 'Enter players..'
        
        Button:
            text: 'Start game!'
            size_hint_y: .2
            on_release: root.first_game_screen(n_players.text)
            on_release: root.manager.current = 'NextGameScreen'


<NextGameScreen>:
    quests_data: quests_data
    answers_data: answers_data
    quests_label: quests_label

    BoxLayout:
        orientation: 'vertical'
        padding: 40

        Button:
            size_hint_y: .3
            text: 'New Game!'
            on_release: app.clear_var()
            on_release: root.manager.current = 'Home'
        
        Button:
            size_hint_y: .3
            text: 'Exit'
            on_release: app.stop()

        Label:
            id: quests_label
            text: 'First Player'

        TextInput:
            id: answers_data
            text: 'Enter answer'
        
        TextInput:
            id: quests_data
            text: 'Enter quest'
        
        Button:
            text: 'Next'
            size_hint_y: .3
            on_release: root.add_data(answers_data.text, quests_data.text, quests_label.text)
        
        Button:
            text: 'The end!'
            size_hint_y: .3
            on_release: root.end()
            on_release: root.manager.current = 'TheEndScreen'
            on_release: root.add_data(answers_data.text, quests_data.text, quests_label.text)
            

<TheEndScreen>:
    end_label: end_label

    BoxLayout:
        orientation: 'vertical'

        TextInput:
            id: end_label
        
        Button:
            size_hint_y: .3
            text: 'Click for update answers...'
            on_release: root.update_answers()
        
        Button:
            size_hint_y: .3
            text: 'New Game!'
            on_release: app.clear_var()
            on_release: root.manager.current = 'Home'
        
        Button:
            size_hint_y: .3
            text: 'Exit'
            on_release: app.stop()

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

        self.answers_data.text = 'Enter answer'
        self.quests_data.text = 'Enter quest'
    
    def end(self):

        TheEndScreen().update_answers()


class TheEndScreen(Screen):

    end_label = ObjectProperty()

    def update_answers(self):

        ans = ''
        for i in range(len(answers)):
            ans += answers[i] + '\n' + quests[i] + '\n'

        self.end_label.text = ans


class ChepuhaApp(App):

    def build(self):

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
