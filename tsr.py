import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit


class Starter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 250, 190)
        self.setWindowTitle('Start_Menu_Game')

        self.btn = QPushButton('Start', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(110, 80)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Hello, unidentified user")
        self.label.adjustSize()
        self.label.move(30, 10)

        self.name_label = QLabel(self)
        self.name_label.setText("Enter a name: ")
        self.name_label.move(30, 40)

        self.name_input = QLineEdit(self)
        self.name_input.move(115, 40)

        self.btn.clicked.connect(self.clicked)

    def hello(self):
        name = self.name_input.text()
        self.label.setText(f"Wellcome a new world!")
        self.label.adjustSize()

    def clicked(self):
        self.second_form = Prologue(self, 'Prologue_of_the_game')
        self.second_form.show()


class Prologue(QWidget):

    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(255, 255, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 1300, 700)
        self.setWindowTitle('Prologue_of_the_game')
        self.move(200, 0)

        ida = ['A long time ago, when gods and humans lived in the same world.',
               'When the higher ones went to heaven and disappeared into this world, the lower ones began to turn into demons.',
               'This is how monsters, spirits and otherworldly forces appeared in the human world. ',
               'Wanting to return to the creators, the demons went to the trick. ',
               'Having obtained hundreds of peoples souls, the kami could open portals to Nakwon.',
               ' The patrons found out about this and decided to close the passage to the dimension as a punishment.',
               'But...',
               'They left behind magical artifacts capable of opening a passage to paradise.',
               'Later people found them, and considered it a sacred relic.',
               'Someone kept them as a talisman, someone sold them, and someone gave them to temples.',
               'People did not know about their true purpose.',
               'The creators wanted to establish a relationship between humans and demons.',
               'The Kami had to earn Rerika through kindness and mercy.',
               'And violence and malice deprived artifacts of power.',
               'But they did not take into account the fact that the relic can be stolen.',
               'And from that moment our story begins.']
        u = "\n".join(ida)

        self.storyboard = QLabel(self)
        self.storyboard.setText(u)
        self.storyboard.adjustSize()
        self.storyboard.move(30, 10)

        self.signature = QLabel(self)
        self.signature.setText('From the legend of gods, demons and human lives. 640 BC.')
        self.signature.adjustSize()
        self.signature.move(640, 650)

        self.conter = QPushButton('Continue', self)
        self.conter.resize(self.conter.sizeHint())
        self.conter.move(640, 610)
        self.conter.clicked.connect(self.clicked)

    def clicked(self):
        self.third_form = Rules(self, 'Game_List_№1')
        self.third_form.show()


class Rules(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(255, 255, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 1370, 375)
        self.setWindowTitle('The rules of the game')
        self.move(150, 0)

        ti = ['The rules of the game are as follows:',
              '1)You can click on the "Yes" and "No" buttons.',
              '2)You entered the name only to continue, your name is Naro and this is not discussed.',
              '3) This game is only in English, so if you dont know it, then pray for good luck.',
              '4)In fact, this is a test game, a full-fledged one will be released on Unity, and before that there will be a pixel mini-game.',
              '5) It is better to close unnecessary windows, do not load your computer.',
              '6) Have a good time :)']
        t = "\n".join(ti)

        self.storyboard_1 = QLabel(self)
        self.storyboard_1.setText(t)
        self.storyboard_1.adjustSize()
        self.storyboard_1.move(30, 10)

        self.signature_1 = QLabel(self)
        self.signature_1.setText('Paranormal Jane / Dary Fox on Glichverse')
        self.signature_1.adjustSize()
        self.signature_1.move(900, 340)

        self.conter_1 = QPushButton('Continue', self)
        self.conter_1.resize(self.conter_1.sizeHint())
        self.conter_1.move(890, 300)
        self.conter_1.clicked.connect(self.clicked)

    def clicked(self):
        self.forth_form = GameList_1(self, 'Game_List_№1')
        self.forth_form.show()


class GameList_1(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 530, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h = ["Greetings, sutorenja-san.",
             "Our monks found you bleeding in the river. ",
             "You were unconscious. ",
             "We've treated you a little. ",
             "Are you feeling well?"]
        h = "\n".join(h)

        self.storyquest_1 = QLabel(self)
        self.storyquest_1.setText(h)
        self.storyquest_1.adjustSize()
        self.storyquest_1.move(30, 10)

        self.button_quest_1 = QPushButton('Yes', self)
        self.button_quest_1.resize(self.button_quest_1.sizeHint())
        self.button_quest_1.move(170, 180)
        self.button_quest_1.clicked.connect(self.clicked_yes)

        self.button_quest_2 = QPushButton('No', self)
        self.button_quest_2.resize(self.button_quest_2.sizeHint())
        self.button_quest_2.move(70, 180)
        self.button_quest_2.clicked.connect(self.clicked_no)

    def clicked_yes(self):
        self.fifth_form = GameList_2_1(self, 'Game_List_№2_1')
        self.fifth_form.show()

    def clicked_no(self):
        self.sixth_form = GameList_2_2(self, 'Game_List_№2_2')
        self.sixth_form.show()


class GameList_2_1(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 590, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h_1 = ["That's good.",
             "The head nun, Shikuyoku-san, wants to see you.",
             "By the way, my name is Nana.",
             "Please wait.",
             "Ok?"]
        h_1 = "\n".join(h_1)

        self.storyquest_2 = QLabel(self)
        self.storyquest_2.setText(h_1)
        self.storyquest_2.adjustSize()
        self.storyquest_2.move(30, 10)

        self.button_quest_3 = QPushButton('Yes', self)
        self.button_quest_3.resize(self.button_quest_3.sizeHint())
        self.button_quest_3.move(170, 180)
        self.button_quest_3.clicked.connect(self.clicked_yes)

        self.button_quest_4 = QPushButton('No', self)
        self.button_quest_4.resize(self.button_quest_4.sizeHint())
        self.button_quest_4.move(70, 180)
        self.button_quest_4.clicked.connect(self.clicked_no)

    def clicked_yes(self):
        self.seventh_form = GameList_3_1(self, 'Game_List_№3_1')
        self.seventh_form.show()

    def clicked_no(self):
        self.eitinth_form = GameList_3_2(self, 'Game_List_№3_2')
        self.eitinth_form.show()


class GameList_3_1(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 530, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h_2 = ["Well, that's nice.",
             "I'll be back soon.",
             "(Click Continue)"]
        h_2 = "\n".join(h_2)

        self.storyquest_4 = QLabel(self)
        self.storyquest_4.setText(h_2)
        self.storyquest_4.adjustSize()
        self.storyquest_4.move(30, 10)

        self.button_quest_7 = QPushButton('Continue', self)
        self.button_quest_7.resize(self.button_quest_7.sizeHint())
        self.button_quest_7.move(170, 180)
        self.button_quest_7.clicked.connect(self.clicked_con)

    def clicked_con(self):
        self.ninth_form = Ender_1(self, 'Further_developments_№1')
        self.ninth_form.show()


class Ender_1(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(199, 21, 133); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 1050, 400)
        self.setWindowTitle('End')
        self.move(200, 0)

        g_1 = ["So...."
               "You waited for the head nun.",
               "She told you that she has your artifact.",
               "And she warned you that you can't publicly kill her - the guards will interfere.",
               "So she makes a deal. You must serve the temple indefinitely.",
               "But this was not to be. Suddenly, the demon pierces her through, killing her.",
               "And at the same time attacks you.",
               "Asks you to tell me where the relic is.",
               "But you refuse and enter into an unequal battle.",
               "After a prolonged fight, Amano-Sensei, the patron of the attacking demon, suddenly appears.",
               "He cursed the Simph for eternal life in the human world and turned you into a toy.",
               "Only by redeeming your sins can you put everything back in its place.",
               "To be continued..."]
        g_1 = "\n".join(g_1)

        self.storyend_1 = QLabel(self)
        self.storyend_1.setText(g_1)
        self.storyend_1.adjustSize()
        self.storyend_1.move(30, 10)


class GameList_3_2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 530, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h_3 = ["How impatient you are.",
               "Where are you in such a hurry?",
               "Better wait until Shokuyoku-san arrives.",
               "(Click Continue)"]
        h_3 = "\n".join(h_3)

        self.storyquest_5 = QLabel(self)
        self.storyquest_5.setText(h_3)
        self.storyquest_5.adjustSize()
        self.storyquest_5.move(30, 10)

        self.button_quest_8 = QPushButton('Continue', self)
        self.button_quest_8.resize(self.button_quest_8.sizeHint())
        self.button_quest_8.move(170, 180)
        self.button_quest_8.clicked.connect(self.clicked_con)

    def clicked_con(self):
        self.tenth_form = Ender_2(self, 'Further_developments_№2')
        self.tenth_form.show()


class Ender_2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(199, 21, 133); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 730, 300)
        self.setWindowTitle('End')
        self.move(400, 0)

        g_2 = ["So....",
               "You didn't wait for the head nun.",
               "You have discovered the loss of a magical artifact.",
               "Perhaps they were taken by nuns.",
               "Suddenly there is an attack by a demon-the fallen god Simph.",
               "He needs an artifact to open the portal.",
               "You engage him in battle.",
               "To be continued...."]
        g_2 = "\n".join(g_2)

        self.storyend_2 = QLabel(self)
        self.storyend_2.setText(g_2)
        self.storyend_2.adjustSize()
        self.storyend_2.move(30, 10)


class GameList_2_2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 530, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h_4 = ["Oh, well, then I'll bring a decoction of herbs.",
               "Don't get up, please.",
               "Can you tell what kind of pain it is?",
               "(Looks worried)"]
        h_4 = "\n".join(h_4)

        self.storyquest_3 = QLabel(self)
        self.storyquest_3.setText(h_4)
        self.storyquest_3.adjustSize()
        self.storyquest_3.move(30, 10)

        self.button_quest_5 = QPushButton('Yes', self)
        self.button_quest_5.resize(self.button_quest_5.sizeHint())
        self.button_quest_5.move(170, 180)
        self.button_quest_5.clicked.connect(self.clicked_yes)

        self.button_quest_6 = QPushButton('No', self)
        self.button_quest_6.resize(self.button_quest_6.sizeHint())
        self.button_quest_6.move(70, 180)
        self.button_quest_6.clicked.connect(self.clicked_no)

    def clicked_yes(self):
        self.eleventh_form = GameList_4_1(self, 'Game_List_№4_1')
        self.eleventh_form.show()

    def clicked_no(self):
        self.twelfth_form = GameList_4_2(self, 'Game_List_№4_2')
        self.twelfth_form.show()


class GameList_4_1(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 670, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h_6 = ["Clearly, it's most likely a wound under the bandages.",
               "I'll put some cold cloth on it now, I hope you feel better.",
               "(Click Continue)"]
        h_6 = "\n".join(h_6)

        self.storyquest_7 = QLabel(self)
        self.storyquest_7.setText(h_6)
        self.storyquest_7.adjustSize()
        self.storyquest_7.move(30, 10)

        self.button_quest_10 = QPushButton('Continue', self)
        self.button_quest_10.resize(self.button_quest_10.sizeHint())
        self.button_quest_10.move(170, 180)
        self.button_quest_10.clicked.connect(self.clicked_con)

    def clicked_con(self):
        self.fourteenth_form = Ender_3(self, 'Further_developments_№3')
        self.fourteenth_form.show()


class Ender_3(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(199, 21, 133); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 600, 300)
        self.setWindowTitle('End')
        self.move(400, 0)

        g_2 = ["The cold numbed the pain for a while.",
               "I began to feel sleepy.",
               "Is it possible to fall asleep forever?",
               "To be continued...."]
        g_2 = "\n".join(g_2)

        self.storyend_3 = QLabel(self)
        self.storyend_3.setText(g_2)
        self.storyend_3.adjustSize()
        self.storyend_3.move(30, 10)


class GameList_4_2(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(127, 199, 255); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 590, 230)
        self.setWindowTitle('Game')
        self.move(400, 0)

        h_6 = ["Oh, my God, a demon is trying to take over you!",
               "Stay calm, I'll bring prayers.",
               "(Click Continue)"]
        h_6 = "\n".join(h_6)

        self.storyquest_7 = QLabel(self)
        self.storyquest_7.setText(h_6)
        self.storyquest_7.adjustSize()
        self.storyquest_7.move(30, 10)

        self.button_quest_10 = QPushButton('Continue', self)
        self.button_quest_10.resize(self.button_quest_10.sizeHint())
        self.button_quest_10.move(170, 180)
        self.button_quest_10.clicked.connect(self.clicked_con)

    def clicked_con(self):
        self.fourteenth_form = Ender_4(self, 'Further_developments_№4')
        self.fourteenth_form.show()


class Ender_4(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.setStyleSheet('background-color: rgb(33, 33, 33); border-color: rgb(18, 18, 18);'
                           ' color: rgb(199, 21, 133); font: 16pt "Pauls Kanji Font";')
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(1000, 1000, 350, 500)
        self.setWindowTitle('End')
        self.move(400, 0)

        g_2 = ["Pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "pain,",
               "and...",
               "silence...",
               "To be continued..."]
        g_2 = "\n".join(g_2)

        self.storyend_4 = QLabel(self)
        self.storyend_4.setText(g_2)
        self.storyend_4.adjustSize()
        self.storyend_4.move(30, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Starter()
    ex.show()
    sys.exit(app.exec())