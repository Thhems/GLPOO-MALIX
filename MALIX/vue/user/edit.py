from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton
from vue.window import BasicWindow
from controller.member_controller import MemberController


class EditUserQt(BasicWindow):
    def __init__(self, member_controller: MemberController, id: str, show_vue: BasicWindow = None):
        self._member_controller = member_controller
        super().__init__()
        self.user_id = id
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.email = QLineEdit()

        self.show_vue = show_vue
        self.setup()
        self.fillform()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("First Name", self.first_name)

        Layout.addRow("Last Name", self.last_name)

        Layout.addRow("Email", self.email)
        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_edit = QPushButton('Edit User', self)
        btn_edit.clicked.connect(self.editUser)
        btn_edit.resize(btn_edit.sizeHint())
        btn_edit.move(90, 100)
        ValidationLayout.addWidget(btn_edit)

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

    def editUser(self):
        # Show subscription formular
        data = {'firstname': self.first_name.text(), 'lastname': self.last_name.text(), 'email': self.email.text(), 'type': 'customer'}
        self._member_controller.update_member(self.user_id, data)
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()

    def fillform(self):
        user = self._member_controller.get_member(self.user_id)
        self.first_name.setText(user['firstname'])
        self.last_name.setText(user['lastname'])
        self.email.setText(user['email'])