import os
import time
from update import *
from labels import * 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.theming import ThemeManager

class Navigation(MDNavigationDrawer):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class HomeScreen(Screen):
    def updateQuestions(self):
        update()
    pass

class TechScreen(Screen):
    index = 0
    question = TECH_QUESTIONS[index]
    correctAnswer = TECH_CORRECT_ANSWERS[index]
    answer_1 = TECH_ANSWERS[index]
    answer_2 = TECH_ANSWERS[index+1]
    answer_3 = TECH_ANSWERS[index+2]
    answer_4 = TECH_ANSWERS[index+3]

    def check_answer(self, button_pressed):
        self.correctAnswer = TECH_CORRECT_ANSWERS[self.index]

        print(self.correctAnswer)
        if button_pressed.name == self.correctAnswer:
            print("Correct")
        else:
            print("Wrong")

        self.changeIndex(1)

    def changeIndex(self, offset):

        if self.index > len(TECH_QUESTIONS):
            index = 0

        self.index = self.index + offset
        self.question = TECH_QUESTIONS[self.index]
        self.ids.question.text = self.question

        self.answer_1 = TECH_ANSWERS[self.index*4]
        self.ids.answer_1.text = self.answer_1

        self.answer_2 = TECH_ANSWERS[self.index*4+1]
        self.ids.answer_2.text = self.answer_2

        self.answer_3 = TECH_ANSWERS[self.index*4+2]
        self.ids.answer_3.text = self.answer_3

        self.answer_4 = TECH_ANSWERS[self.index*4+3]
        self.ids.answer_4.text = self.answer_4


    def skip(self, button_pressed):
        self.changeIndex(1)

    def back(self, button_pressed):
        self.changeIndex(-1)
    pass

class GeneralScreen(Screen):
    index = 0
    question = GEN_QUESTIONS[index]
    correctAnswer = GEN_CORRECT_ANSWERS[index]
    answer_1 = GEN_ANSWERS[index]
    answer_2 = GEN_ANSWERS[index+1]
    answer_3 = GEN_ANSWERS[index+2]
    answer_4 = GEN_ANSWERS[index+3]

    def check_answer(self, button_pressed):
        self.correctAnswer = GEN_CORRECT_ANSWERS[self.index]

        print(self.correctAnswer)
        if button_pressed.name == self.correctAnswer:
            print("Correct")
        else:
            print("Wrong")

        self.changeIndex(1)

    def changeIndex(self, offset):

        if self.index > len(GEN_QUESTIONS):
            index = 0

        self.index = self.index + offset
        self.question = GEN_QUESTIONS[self.index]
        self.ids.question.text = self.question

        self.answer_1 = GEN_ANSWERS[self.index*4]
        self.ids.answer_1.text = self.answer_1

        self.answer_2 = GEN_ANSWERS[self.index*4+1]
        self.ids.answer_2.text = self.answer_2

        self.answer_3 = GEN_ANSWERS[self.index*4+2]
        self.ids.answer_3.text = self.answer_3

        self.answer_4 = GEN_ANSWERS[self.index*4+3]
        self.ids.answer_4.text = self.answer_4


    def skip(self, button_pressed):
        self.changeIndex(1)

    def back(self, button_pressed):
        self.changeIndex(-1)
    pass

class ExtraScreen(Screen):
    index = 0
    question = EXTRA_QUESTIONS[index]
    correctAnswer = EXTRA_CORRECT_ANSWERS[index]
    answer_1 = EXTRA_ANSWERS[index]
    answer_2 = EXTRA_ANSWERS[index+1]
    answer_3 = EXTRA_ANSWERS[index+2]
    answer_4 = EXTRA_ANSWERS[index+3]

    def check_answer(self, button_pressed):
        self.correctAnswer = EXTRA_CORRECT_ANSWERS[self.index]

        print(self.correctAnswer)
        if button_pressed.name == self.correctAnswer:
            print("Correct")
        else:
            print("Wrong")

        self.changeIndex(1)

    def changeIndex(self, offset):

        if self.index > len(EXTRA_QUESTIONS):
            index = 0

        self.index = self.index + offset
        self.question = EXTRA_QUESTIONS[self.index]
        self.ids.question.text = self.question

        self.answer_1 = EXTRA_ANSWERS[self.index*4]
        self.ids.answer_1.text = self.answer_1

        self.answer_2 = EXTRA_ANSWERS[self.index*4+1]
        self.ids.answer_2.text = self.answer_2

        self.answer_3 = EXTRA_ANSWERS[self.index*4+2]
        self.ids.answer_3.text = self.answer_3

        self.answer_4 = EXTRA_ANSWERS[self.index*4+3]
        self.ids.answer_4.text = self.answer_4


    def skip(self, button_pressed):
        self.changeIndex(1)

    def back(self, button_pressed):
        self.changeIndex(-1)
    pass

class Screen_Manager(ScreenManager):
    pass
    

class MainApp(App):
    theme_cls = ThemeManager()
    theme_cls.theme_style = 'Dark'
    #theme_cls.primary_palette = 'Grey'
    title = "Ham Radio Pracitce Quiz"
    sm = Screen_Manager()

    def build(self):
        #main_widget = Builder.load_file(os.path.join(os.path.dirname(__file__), "./main.kv"))
        self.sm.add_widget(HomeScreen(name='Home'))
        self.sm.add_widget(TechScreen(name='Technician'))
        self.sm.add_widget(GeneralScreen(name='General'))
        self.sm.add_widget(ExtraScreen(name='Extra'))

        return self.sm


if __name__ == '__main__':
    MainApp().run()