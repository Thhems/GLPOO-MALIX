from controller.liste_controller import ListController
from vue.window import BasicWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton
from vue.user.show import ListUserQt
from vue.event.show import ListEventQt
from controller.member_controller import MemberController
from controller.event_controller import EventController



class MenuWindow(BasicWindow):
    def __init__(self, member_controller: MemberController, event_controller: EventController, resa_controller: ListController):
        self._event_controller = event_controller
        self._member_controller = member_controller
        self._resa_controller = resa_controller
        super().__init__()
        self.listUserWindow = None
        self.listEventWindow = None

        self.setup()

    def setup(self):
        btn_listm = QPushButton('Liste des utilisateurs', self)
        btn_listm.resize(btn_listm.sizeHint())
        btn_listm.move(80, 100)
        btn_listm.clicked.connect(self.list_user)

        btn_liste = QPushButton('Liste des events', self)
        btn_liste.resize(btn_liste.sizeHint())
        btn_liste.move(0, 0)
        btn_liste.clicked.connect(self.list_event)

        btn_quit = QPushButton('Quitter', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        layout = QVBoxLayout()
        layout.addWidget(btn_listm)
        layout.addWidget(btn_liste)
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
