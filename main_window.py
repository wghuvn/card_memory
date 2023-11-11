from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton,QLabel, QSpinBox
from PyQt5.QtCore import Qt
win_card = QWidget()
win_card.resize(600,500)
win_card.move(300,300)
win_card.setWindowTitle("Memory Card")

btn_menu = QPushButton('Menu')
btn_rest = QPushButton('Відпочити')

sb_rest = QSpinBox()
sb_rest.setValue(30)

lb_rest = QLabel('хвилини')

lb_question=QLabel(' п')

q_rb1 = QRadioButton('')
q_rb2 = QRadioButton('')
q_rb3 = QRadioButton('')
q_rb4 = QRadioButton('')

qb_group = QButtonGroup()
qb_group.addButton(q_rb1)
qb_group.addButton(q_rb2)
qb_group.addButton(q_rb3)
qb_group.addButton(q_rb4)

question_group = QGroupBox("Варіанти відповідей")

lineH_1 = QHBoxLayout()
lineH_1.addWidget(btn_menu)
lineH_1.addWidget(btn_rest)
lineH_1.addWidget(sb_rest)
lineH_1.addWidget(lb_rest)

lineH_2 = QHBoxLayout()
lineH_2.addWidget(lb_question)
lineV_main = QVBoxLayout()
lineV_main.addWidget(question_group)
lineV_1 = QVBoxLayout()
lineV_1.addWidget(q_rb1)
lineV_1.addWidget(q_rb3)

lineV_2 = QVBoxLayout()
lineV_2.addWidget(q_rb2)
lineV_2.addWidget(q_rb4)

lineH_3 = QHBoxLayout()
lineH_3.addLayout(lineV_1)
lineH_3.addLayout(lineV_2)

question_group.setLayout(lineH_3)

lineV_main.addLayout(lineH_1)
lineV_main.addLayout(lineH_2)

win_card.setLayout(lineV_main)
