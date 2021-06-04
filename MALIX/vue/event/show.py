from PySide6.QtWidgets import QListWidget, QGridLayout,  QVBoxLayout, QPushButton, QHBoxLayout
from vue.event.add import AddEventQt
from vue.event.edit import EditEventQt
from vue.event.delete import DeleteEventQt
from vue.event.search import SearchEventQt
from vue.window import BasicWindow
from controller.event_controller import EventController


class ListEventQt(BasicWindow):

    def __init__(self, event_controller: EventController):
        super().__init__()

        self._event_controller = event_controller
        self.addEventWindow = None
        self.editEventWindow = None
        self.deleteEventWindow = None
        self.searchEventWindow = None
        self.layout = QHBoxLayout()

        self.listlayout = QGridLayout()
        self.listwidget = QListWidget()

        self.btn_add_event = QPushButton('Add event', self)
        self.btn_edit_event = QPushButton('Edit event', self)
        self.btn_delete_event = QPushButton('Delete event', self)
        self.btn_search_event = QPushButton('Search event', self)

        self.event_mapping = {}

        self.list()
        self.side_menu()
        self.setLayout(self.layout)

    def list(self):

        self.listwidget.clear()
        index = 0
        for event in self._event_controller.list_events():
            self.listwidget.insertItem(index, "* %s %s (%s) - %s %s" % (
                event['name'],
                event['date'],
                event['places'],
                event['lieu'],
                event['prix']))
            self.event_mapping[index] = event
            index += 1

        self.listwidget.clicked.connect(self.clicked)
        self.listwidget.resize(self.listwidget.sizeHint())
        self.listwidget.move(0, 60)
        self.listlayout.addWidget(self.listwidget)
        self.layout.addLayout(self.listlayout)

    def side_menu(self):

        self.btn_add_event.resize(self.btn_add_event.sizeHint())
        self.btn_add_event.move(60, 20)
        self.btn_add_event.clicked.connect(self.add_event)

        self.btn_edit_event.resize(self.btn_edit_event.sizeHint())
        self.btn_edit_event.move(60, 40)
        self.btn_edit_event.setEnabled(False)
        self.btn_edit_event.clicked.connect(self.edit_event)

        self.btn_delete_event.resize(self.btn_delete_event.sizeHint())
        self.btn_delete_event.move(60, 60)
        self.btn_delete_event.setEnabled(False)
        self.btn_delete_event.clicked.connect(self.delete_event)

        self.btn_search_event.resize(self.btn_edit_event.sizeHint())
        self.btn_search_event.move(60, 80)
        self.btn_search_event.clicked.connect(self.search_event)

        btn_quit = QPushButton('Close', self)
        btn_quit.clicked.connect(self.close)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(90, 100)

        buttonlayout = QVBoxLayout()
        buttonlayout.addWidget(self.btn_add_event)
        buttonlayout.addWidget(self.btn_edit_event)
        buttonlayout.addWidget(self.btn_delete_event)
        buttonlayout.addWidget(self.btn_search_event)
        buttonlayout.addWidget(btn_quit)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('event menu')
        self.layout.addLayout(buttonlayout)

    def clicked(self):
        item = self.listwidget.currentItem()
        self.btn_edit_event.setEnabled(True)
        self.btn_delete_event.setEnabled(True)
        print(item.text())

    def refresh(self):
        self.list()
        self.show()

    def add_event(self):
        if self.addEventWindow is None:
            self.addEventWindow = AddEventQt(self._member_controller, self)
        self.addEventWindow.show()

    def edit_event(self):
        if self.editEventWindow is None:
            event = self.member_mapping[self.listwidget.currentRow()]
            self.editEventWindow = EditEventQt(self._member_controller, event['id'], self)
        self.editEventWindow.show()

    def delete_event(self):
        if self.deleteEventWindow is None:
            event = self.member_mapping[self.listwidget.currentRow()]
            self.deleteEventWindow = DeleteEventQt(self._member_controller, event['id'], self)
        self.deleteEventWindow.show()

    def search_event(self):
        if self.searchEventWindow is None:
            self.searchEventWindow = SearchEventQt(self._member_controller, self)
        self.searchEventWindow.show()
