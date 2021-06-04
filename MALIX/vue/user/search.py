from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent
from vue.user.edit import EditUserQt
from vue.window import BasicWindow
from controller.member_controller import MemberController


class SearchUserQt(BasicWindow):

    def __init__(self, member_controller: MemberController, show_vue: BasicWindow = None):
        self._member_controller = member_controller
        super().__init__()
        ##
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.editUserWindow = None

        self.show_vue = show_vue
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("First Name", self.first_name)

        Layout.addRow("Last Name", self.last_name)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_search = QPushButton('Search User', self)
        btn_search.clicked.connect(self.searchUser)
        btn_search.resize(btn_search.sizeHint())
        btn_search.move(90, 100)
        ValidationLayout.addWidget(btn_search)
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

    def quitEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit ?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()

    def get_user_id(self, userfromlist:str):
        for member in self.members:
            if "* " + member['firstname'] + " " + member['lastname'] + " (" + member['email'] + ") - " + member['type'] == userfromlist:
                print(member['id'])
                return member['id']

    def searchUser(self):
        print(self.first_name.text() + self.last_name.text())
        user = self._member_controller.search_member(self.first_name.text(), self.last_name.text())
        if self.editUserWindow is None:
            self.editUserWindow = EditUserQt(self._member_controller, user['id'])
        self.editUserWindow.show()
        if self.show_vue is not None:
            self.show_vue.refresh()
        self.close()
