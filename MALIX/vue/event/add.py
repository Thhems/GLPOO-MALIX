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

        Layout.addRow("Nom", self.name)

        Layout.addRow("date", self.date)

        Layout.addRow("places", self.places)

        Layout.addRow("lieu", self.lieu)

        Layout.addRow("prix", self.prix)


        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Ajouter l evenement', self)
        btn_add.clicked.connect(self.addEvent)
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
        data = {'name': self.name.text() ,
                'date': self.date.text(),
                'places': self.places.text(),
                'lieu': self.lieu.text(),
                'prix': self.prix.text()}
        print(data)

        self._event_controller.create_event(data)

        events = self._event_controller.list_events()

        print("Events: ")
        for event in events:
            print("Nom:%s Date:%s Nb places:%s  Lieu:%s  Prix:%s " % (
                event['name'],
                event['date'].capitalize(),
                event['places'],
                event['lieu'],
                event['prix']))
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

