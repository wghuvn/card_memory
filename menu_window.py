from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox,\
    QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QLineEdit
from PyQt5.QtCore import Qt

menu_window = QWidget()

btn_add_question=QPushButton("Додати питання")
btn_clear_question=QPushButton("Очистити")
btn_back = QPushButton("Назад")

lb_add_question = QLabel("Введіть запитання:")
lb_add_answer = QLabel("Введіть правильну відповідь:")
lb_add_wrong1 = QLabel("Введіть першу неправильну відповідь:")
lb_add_wrong2= QLabel("Введіть другу неправильну відповідь:")
lb_add_wrong3 = QLabel("Введіть третю неправильну відповідь:")
lb_stats = QLabel()
lb_stats_title = QLabel("Статистика")

qle_question = QLineEdit()
qle_answer = QLineEdit()
qle_wrong1 = QLineEdit()
qle_wrong2 = QLineEdit()
qle_wrong3 = QLineEdit()

v_lb = QVBoxLayout()
v_lb.addWidget(lb_add_question)
v_lb.addWidget(lb_add_answer)
v_lb.addWidget(lb_add_wrong1)
v_lb.addWidget(lb_add_wrong2)
v_lb.addWidget(lb_add_wrong3)

v_qle = QVBoxLayout()
v_qle.addWidget(qle_question)
v_qle.addWidget(qle_answer)
v_qle.addWidget(qle_wrong1)
v_qle.addWidget(qle_wrong2)
v_qle.addWidget(qle_wrong3)

h_creat_question = QHBoxLayout()
h_creat_question.addLayout(v_lb)
h_creat_question.addLayout(v_qle)

h_question_buttons =QHBoxLayout()
h_question_buttons.addWidget(btn_add_question)
h_question_buttons.addWidget(btn_clear_question)

v_main = QVBoxLayout()
v_main.addLayout(h_creat_question)
v_main.addLayout(h_question_buttons)
v_main.addWidget(lb_stats_title)
v_main.addWidget(lb_stats)
v_main.addWidget(btn_back)

menu_window.setLayout(v_main)

menu_window.resize(400,600)