from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from controller.event_controller import EventController
from vue.window import BasicWindow


class AddEventQt(BasicWindow, EventController):

    def __init__(self, event_controller: EventController, show_vue: BasicWindow = None):
        self._event_controller = event_controller
        super().__init__()
        ##
        self.name = QLineEdit()
        self.date = QLineEdit()
        self.places = QLineEdit()
        self.lieu = QLineEdit()
        self.prix = QLineEdit()

        self.show_vue = show_vue
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Nom", self.first_name)

        Layout.addRow("date", self.last_name)

        Layout.addRow("places", self.email)

        Layout.addRow("lieu", self.email)

        Layout.addRow("prix", self.email)


        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Ajouter l evenement', self)
        btn_add.clicked.connect(self.add)
        btn_add.resize(btn_add.sizeHint())
        btn_add.move(90, 100)
        ValidationLayout.addWidget(btn_add)
        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Close', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def addEvent(self):
        # Show subscription formular
        data = {'Nom': self.ask_name.text(),
                'date': self.ask_date.text(),
                'places': self.ask_places.text(),
                'lieu': self.ask_lieu.currentText(),
                'prix': self.ask_prix.currentText()}
        print(data)
        self.create_event(data)

        events = self.list_events()

        print("Events: ")
        for event in events:
            print("* %s %s (%s) - %s  %s" % (
                data['name'].capitalize(),
                data['date'].capitalize(),
                data['places'],
                data['lieu'],
                data['prix']))
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

