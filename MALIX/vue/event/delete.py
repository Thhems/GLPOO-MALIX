from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton

from controller.event_controller import EventController
from vue.window import BasicWindow
from controller.member_controller import MemberController


class DeleteEventQt(BasicWindow):
    def __init__(self, event_controller: EventController, id: str, show_vue: BasicWindow = None):
        self._event_controller = event_controller
        super().__init__()
        self.event_id = id
        self.name = QLineEdit()
        self.date = QLineEdit()
        self.places = QLineEdit()
        self.lieu = QLineEdit()
        self.prix = QLineEdit()

        self.show_vue = show_vue
        self.setup()
        self.fillform()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout
        self.name.setEnabled(False)
        Layout.addRow("Name", self.name)

        self.date.setEnabled(False)
        Layout.addRow("date", self.date)

        self.places.setEnabled(False)
        Layout.addRow("places", self.places)

        self.lieu.setEnabled(False)
        Layout.addRow("lieu", self.lieu)

        self.prix.setEnabled(False)
        Layout.addRow("prix", self.prix)
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_delete = QPushButton('Delete Event', self)
        btn_delete.clicked.connect(self.deleteEvent())
        btn_delete.resize(btn_delete.sizeHint())
        btn_delete.move(90, 100)
        ValidationLayout.addWidget(btn_delete)

        # Add some checkboxes to the layout
        btn_cancel = QPushButton('Quit', self)
        btn_cancel.clicked.connect(self.quitEvent)
        btn_cancel.resize(btn_cancel.sizeHint())
        btn_cancel.move(90, 100)
        ValidationLayout.addWidget(btn_cancel)
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(Layout)
        outerLayout.addLayout(ValidationLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

    def deleteEvent(self):
        # Show subscription formular
        self._event_controller.delete_event(self.event_id)
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

    def fillform(self):
        event = self._event_controller.get_event(self.event_id)
        self.name.setText(event['name'])
        self.date.setText(event['date'])
        self.places.setText(str(event['places']))
        self.lieu.setText(event['lieu'])
        self.prix.setText(str(event['prix']))
