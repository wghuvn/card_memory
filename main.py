from PyQt5.QtWidgets import QApplication
from random import choice, shuffle
a = QApplication([])
from time import sleep
from main_window import *
from menu_window import *


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
    def get_attempts(self):
        return self.attempts
    def get_success(self):
        return self.success


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
    RadioGroup.setExclusive(False)
    for answer in radio_list:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно')
                current_question.got_right()
            else:
                lb_result.setText("Неправильно")
                current_question.got_wrong()
            answer.setChecked(False)  

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

def switch_window_to_menu():
    window.hide()
    count_stats()
    menu_window.show()

def switch_menu_to_window():
    window.show()
    menu_window.hide()

def creat_question():
    if len(qle_question.text())>2:
        question_text = qle_question.text()
        if len(qle_answer.text())>2:
            question_answer = qle_answer.text()
            if len(qle_wrong1.text())>2:
                question_wrong1 = qle_wrong1.text()
                if len(qle_wrong2.text())>2:
                    question_wrong2 = qle_wrong2.text()
                    if len(qle_wrong1.text())>2:
                        question_wrong3 = qle_wrong3.text()
                        question = Question(question_text,question_answer, question_wrong1, question_wrong2, question_wrong3)
                        question_list.append(question)

def clear_question():
    qle_question.clear()  
    qle_answer.clear()
    qle_wrong1.clear()
    qle_wrong2.clear()
    qle_wrong3.clear()  


def count_stats():
    attempts_sum = 0
    success_sum = 0
    for question in question_list:
        attempts_sum += question.get_attempts()
        success_sum += question.get_success()
    rate = success_sum / attempts_sum*100
    text = f'Разів відповіли: {attempts_sum}\n' \
    f'Вірних відповідей: {success_sum}\n' \
    f'Успішність: {round(rate)}%'
    lb_stats.setText(text)

btn_rest.clicked.connect(rest)
btn_next.clicked.connect(switch_screen)
btn_menu.clicked.connect(switch_window_to_menu)
btn_back.clicked.connect(switch_menu_to_window)
btn_add_question.clicked.connect(creat_question)
btn_clear_question.clicked.connect(clear_question)
window.show()
a.exec_()


    

