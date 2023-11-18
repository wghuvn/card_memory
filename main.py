from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
a = QApplication([])
from time import sleep
from main_window import *


class Question():
    def __init__(self,text, right_answer, ans2,ans3, ans4):
        self.text = text
        self.right_answer = right_answer
        self.ans2= ans2
        self.ans3 = ans3
        self.ans4 = ans4
        self.attempts = 0
        self.success = 0
    def get_text(self):
        return self.text
    def got_right(self):
        self.attempts += 1
        self.success += 1
    def got_wrong(self):
        self.attempts +=1


question1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
question2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
question3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
question4 = Question('Число', 'number', 'digit', 'amount', 'summary')


radio_list = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
question_list = [question1, question2,question3, question4]

def new_question():
    global current_question
    current_question = choice(question_list)
    lb_question.setText(current_question.get_text())
    lb_right_answer.setText(current_question.right_answer)
    shuffle(radio_list)
    radio_list[0].setText(current_question.right_answer)
    radio_list[1].setText(current_question.ans2)
    radio_list[2].setText(current_question.ans3)
    radio_list[3].setText(current_question.ans4)

new_question()

def check_result():
    for answer in radio_list:
        if answer.isChecked():
            if answer.text() == current_question.text:
                lb_result.setText('Правильно')
                answer.got_right()
        else:
            lb_result.setText("Неправильно")
            

def switch_screen():
    if btn_next.text() == "Відповісти":
        check_result()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText("Наступне питання")
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText("Відповісти")

def rest():
    window.hide()
    sleep(sp_rest.value()*60)
    window.show()

btn_rest.clicked.connect(rest)
btn_next.clicked.connect(switch_screen)

window.show()
a.exec_()


    

