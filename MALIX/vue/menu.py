from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton
from vue.user.show import ListUserQt
from vue.event.show import ListEventQt
from controller.member_controller import MemberController
from controller.event_controller import EventController



class MenuWindow(BasicWindow):
    def __init__(self, member_controller: MemberController, event_controller: EventController):
        self._event_controller = event_controller
        self._member_controller = member_controller
        super().__init__()
        self.listUserWindow = None
        self.listEventWindow = None

        self.setup()

    def setup(self):
        btn_list = QPushButton('Liste des utilisateurs', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(0, 0)
        btn_list.clicked.connect(self.list_user)

        btn_list = QPushButton('Liste des events', self)
        btn_list.resize(btn_list.sizeHint())
        btn_list.move(100, 0)
        btn_list.clicked.connect(self.list_event)

        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        layout = QVBoxLayout()
        layout.addWidget(btn_list)
        layout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Shop application Menu')
        self.setLayout(layout)
        self.show()

    def list_user(self):
        if self.listUserWindow is None:
            self.listUserWindow = ListUserQt(self._member_controller)
            self.listUserWindow.show()

    def list_event(self):
        if self.listEventWindow is None:
            self.listEventWindow = ListEventQt(self._event_controller)
            self.listEventWindow.show()
