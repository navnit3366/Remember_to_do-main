import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc
import screeninfo as si
import sys
from visuals.visual_functions import *


class widget_settings(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = 500
        self.window_height = 700
        self.window_size = list(str(si.get_monitors())[9:-2].split())
        self.screen_width = int(self.window_size[2].removeprefix("width=").removesuffix(","))
        self.screen_height = int(self.window_size[3].removeprefix("height=").removesuffix(","))

        self.setWindowFlag(qc.Qt.FramelessWindowHint)
        self.setWindowIcon(qg.QIcon("images/image3.png"))
        self.setWindowTitle("  Settings")
        self.setGeometry(self.screen_width-self.window_width, self.screen_height-self.window_height-300, self.window_width, self.window_height)
        self.setStyleSheet("background-color: darkslategray;")

        self.time_box = qw.QComboBox(self)
        self.time_box.setStyleSheet("QComboBox{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;}  QComboBox::hover{background-color: #547c7d}")
        self.time_box.setFixedSize(460, 60)
        self.time_box.addItems(set_time_spin()[0])
        self.time_box.setCurrentText(set_time_spin()[1])
        self.time_box.move(20, 20)


        self.layout_list = qw.QVBoxLayout()
        self.scroll_area = qw.QScrollArea(self)
        self.layout_list.setAlignment(qc.Qt.AlignTop)
        self.widget_scroll = qw.QWidget()
        self.scroll_area.setStyleSheet("background-color: #316b6c; border-radius: 10px;")
        self.scroll_area.setFixedSize(460, 400)
        self.scroll_area.move(20, 100)

        self.deleted_tasks = []
        for i in get_all_tasks():
            object = qw.QPushButton()
            object.setFixedSize(400, 70)
            object.setIcon(qg.QIcon("images/image_add.png"))
            object.setIconSize(qc.QSize(50, 50))
            object.setText(i)
            object.setStyleSheet("QPushButton{background-color: darkslategray; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px; text-align: left;} QPushButton::hover{background-color: #547c7d}")
            object.clicked.connect(self.delete)
            self.layout_list.addWidget(object)
        self.widget_scroll.setLayout(self.layout_list)

        self.scroll_area.setVerticalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.widget_scroll)


        self.task_line = qw.QLineEdit(self)
        self.task_line.setPlaceholderText("     max 25 letters...")
        self.task_line.setStyleSheet("QLineEdit{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;} QLineEdit::focus{background-color: #547c7d}")
        self.task_line.setFixedSize(460, 60)
        self.task_line.move(20, 520)
        
        self.added_tasks = []
        self.add_but = qw.QPushButton("Add", self)
        self.add_but.setStyleSheet("QPushButton{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;} QPushButton::hover{background-color: #547c7d}")
        self.add_but.setFixedSize(225, 60)
        self.add_but.move(20, 600)
        self.add_but.clicked.connect(self.add)

        self.save_but = qw.QPushButton("Save", self)
        self.save_but.setStyleSheet("QPushButton{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;} QPushButton::hover{background-color: #547c7d}")
        self.save_but.setFixedSize(225, 60)
        self.save_but.move(255, 600)
        self.save_but.clicked.connect(self.save)


    def delete(self):
        but = self.sender()
        if but.text() not in self.deleted_tasks:
            self.deleted_tasks.append(but.text())
            but.setIcon(qg.QIcon("images/image_delete.png"))
        else:
            index = self.deleted_tasks.index(but.text())
            self.deleted_tasks.pop(index)
            but.setIcon(qg.QIcon("images/image_add.png"))
    
    def add(self):
        task = self.task_line.text()
        if len(task) <= 25 and not len(task) < 1:
            self.task_line.setText("")
            self.task_line.setPlaceholderText("     added task...")
            self.added_tasks.append(task)
        else:
            self.task_line.setText("")
            self.task_line.setPlaceholderText("     task was too long...")
    
    def save(self):
        self.w = widget_list()
        self.w.show()
        self.close()
        delete_tasks(tasks=self.deleted_tasks)
        add_tasks(tasks=self.added_tasks)
        save_time(self.time_box.currentText())


class widget_list(qw.QWidget):
    def __init__(self):
        super().__init__()

        self.window_width = 500
        self.window_height = 700
        self.window_size = list(str(si.get_monitors())[9:-2].split())
        self.screen_width = int(self.window_size[2].removeprefix("width=").removesuffix(","))
        self.screen_height = int(self.window_size[3].removeprefix("height=").removesuffix(","))

        self.setWindowFlag(qc.Qt.FramelessWindowHint)
        self.setWindowIcon(qg.QIcon("images/image2.png"))
        self.setWindowTitle("To Do List")
        self.setGeometry(self.screen_width-self.window_width, self.screen_height-self.window_height-300, self.window_width, self.window_height)
        self.setStyleSheet("background-color: darkslategray;")
        
        self.setting_but = qw.QPushButton("   Settings", self)
        self.setting_but.setStyleSheet("QPushButton{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;} QPushButton::hover{background-color: #547c7d}")
        self.setting_but.setIcon(qg.QIcon("images/image3.png"))
        self.setting_but.setIconSize(qc.QSize(40, 40))
        self.setting_but.setFixedSize(250, 60)
        self.setting_but.move(230, 20)
        self.setting_but.clicked.connect(self.open_settings)


        self.layout_list = qw.QVBoxLayout()
        self.scroll_area = qw.QScrollArea(self)
        self.layout_list.setAlignment(qc.Qt.AlignTop)
        self.widget_scroll = qw.QWidget()
        self.scroll_area.setStyleSheet("background-color: #316b6c; border-radius: 10px;")
        self.scroll_area.setFixedSize(460, 500)
        self.scroll_area.move(20, 100)

        self.checked_tasks = []
        for i in get_tasks():
            object = qw.QPushButton()
            object.setFixedSize(400, 70)
            object.setIcon(qg.QIcon("images/image_unchecked.png"))
            object.setIconSize(qc.QSize(60, 60))
            object.setText(i)
            object.setStyleSheet("QPushButton{background-color: darkslategray; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px; text-align: left;} QPushButton::hover{background-color: #547c7d}")
            object.clicked.connect(self.checked)
            self.layout_list.addWidget(object)
        self.widget_scroll.setLayout(self.layout_list)

        self.scroll_area.setVerticalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(qc.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.widget_scroll)


        self.close_but = qw.QPushButton("OK", self)
        self.close_but.setStyleSheet("QPushButton{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;} QPushButton::hover{background-color: #547c7d}")
        self.close_but.setFixedSize(460, 60)
        self.close_but.move(20, 620)
        self.close_but.clicked.connect(self.save)

    def open_settings(self):
        self.close()
        self.w = widget_settings()
        self.w.show()
    
    def save(self):
        update_tasks_made(self.checked_tasks)
        self.close()

    def checked(self):
        but = self.sender()
        if but.text() not in self.checked_tasks:
            self.checked_tasks.append(but.text())
            but.setIcon(qg.QIcon("images/image_checked.png"))
        else:
            index = self.checked_tasks.index(but.text())
            self.checked_tasks.pop(index)
            but.setIcon(qg.QIcon("images/image_unchecked.png"))


class widget_alert(qw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.window_width = 500
        self.window_height = 130
        self.window_size = list(str(si.get_monitors())[9:-2].split())
        self.screen_width = int(self.window_size[2].removeprefix("width=").removesuffix(","))
        self.screen_height = int(self.window_size[3].removeprefix("height=").removesuffix(","))
        
        self.setWindowFlag(qc.Qt.FramelessWindowHint)
        self.setWindowIcon(qg.QIcon("images/image.png"))
        self.setWindowTitle("To Do Alert")
        self.setGeometry(self.screen_width-self.window_width, self.screen_height-self.window_height-150, self.window_width, self.window_height)
        self.setStyleSheet("background-color: darkslategray;")

        self.widget = qw.QWidget()
        self.layout = qw.QHBoxLayout()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        def later_butf():
            self.close()

        self.img_but = qw.QPushButton()
        self.img_but.resize(120, 120)
        self.img_but.setIcon(qg.QIcon("images/image.png"))
        self.img_but.setIconSize(qc.QSize(120, 120))
        self.img_but.setStyleSheet("QPushButton{background-color: darkslategray; border-radius: 10px;} QPushButton::hover{background-color: #547c7d;}")
        self.layout.addWidget(self.img_but)
        self.img_but.clicked.connect(self.check_list_butf)

        self.lab = qw.QLabel(text="You didn't made all\nof your tasks today!")
        self.lab.setStyleSheet("font-family: Comic Sans Ms; color: white; font-size: 25px; background-color: #316b6c; padding: 15px; border-radius: 10px;")
        self.layout.addWidget(self.lab)

        self.but = qw.QPushButton(text="\nX\n")
        self.but.resize(5, 120)
        self.but.setStyleSheet("QPushButton{background-color: #316b6c; color: white; font-size: 30px; font-family: Comic Sans MS; border-radius: 10px;} QPushButton::hover{background-color: #547c7d}")
        self.layout.addWidget(self.but)
        self.but.clicked.connect(later_butf)

    def check_list_butf(self):
        self.close()
        self.w = widget_list()
        self.w.show()

def run():
    app = qw.QApplication(sys.argv)
    w = widget_alert()
    w.show()
    app.exec_()

def settings():
    app = qw.QApplication(sys.argv)
    w = widget_settings()
    w.show()
    app.exec_()
