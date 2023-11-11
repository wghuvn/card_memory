from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
a = QApplication([])

from main_window import *
win_card.show()
a.exec_()

class Question():
    def __init__(self,text,right_answer,ans2,ans3,ans4):
        self.text = text
        self.right_answer = right_answer
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.attemps = 0
        self.success = 0
    def get_text(self):
        return self.text
    def got_right(self):
        self.attemps +=1
        self.success +=1
    def got_wrong(self):
        self.attemps +=1
        
question1 = Question("Яблуко","apple","application","pinapple","apply")
question2 = Question("Дім","house","horse","hurry","hour")
question3 = Question("Миша","mouse","mouth","muse","museum")
question4 = Question("Число","number","digit","amount","summary")

radio_list = [q_rb1, q_rb2,q_rb3, q_rb4]
question_list = [question1,question2,question3,question4]
current_question = question1
def new_question():
    current_question = choice(shuffle(question_list))
    lb_question.setText(current_question.get_text())
    shuffle(radio_list)
    radio_list[0].setText(current_question.right_answer)
    radio_list[1].setText(current_question.ans2)
    radio_list[2].setText(current_question.ans3)
    radio_list[3].setText(current_question.ans4)
new_question()

    

