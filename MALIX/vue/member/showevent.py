from PySide6.QtWidgets import QListWidget, QGridLayout, QVBoxLayout, QPushButton, QHBoxLayout
from vue.event.add import AddEventQt
from vue.event.edit import EditEventQt
from vue.event.delete import DeleteEventQt
from vue.window import BasicWindow
from controller.event_controller import EventController


class ListEventQtUser(BasicWindow):

    def __init__(self, event_controller: EventController):
        super().__init__()

        self._event_controller = event_controller
        self.addEventWindow = None
        self.editEventWindow = None
        self.deleteEventWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_subscribe_event = QPushButton('S inscrire', self)
        self.btn_unsubscribe_event = QPushButton('Se desinscrire', self)

        self.event_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for event in self._event_controller.list_events():
            self.listwidget.insertItem(index, "%s le %s à %s, Place(s) restante(s): %s  Prix: %s " % (
                event['name'],
                event['date'],
                event['lieu'],
                event['places'],
                event['prix']))
            self.event_mapping[index] = event
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def side_menu(self):

        self.btn_subscribe_event.resize(self.btn_subscribe_event.sizeHint())
        self.btn_subscribe_event.move(60, 20)
        self.btn_subscribe_event.setEnabled(False)
        self.btn_subscribe_event.clicked.connect(self.subscribe_event)

        self.btn_unsubscribe_event.resize(self.btn_unsubscribe_event.sizeHint())
        self.btn_unsubscribe_event.move(60, 40)
        self.btn_unsubscribe_event.setEnabled(False)
        self.btn_unsubscribe_event.clicked.connect(self.unsubscribe_event)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_subscribe_event)
        buttonlayout.addWidget(self.btn_unsubscribe_event)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 600, 200)
        self.setWindowTitle('Liste des événements')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_subscribe_event.setEnabled(True)
        self.btn_unsubscribe_event.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def subscribe_event(self):
        if self.subscribeEventWindow is None:
            print("inscription event")
        self.subscribeEventWindow.show()

    def unsubscribe_event(self):
        if self.unsubscribeEventWindow is None:
            print("desinscription event")
        self.unsubscribeEventWindow.show()
