from PySide6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox
from vue.window import BasicWindow
from controller.member_controller import MemberController
from controller.liste_controller import ListController
from vue.member_vue import MemberVue


class ConnexionQt(BasicWindow):

    def __init__(self, member_controller: MemberController, member_vue: MemberVue, liste_controller: ListController,
                 show_vue: BasicWindow = None):
        self._member_controller = member_controller
        self._member_vue = member_vue
        self._liste_controller = liste_controller
        super().__init__()
        ##

        self.email = QLineEdit()
        self.last_name = QLineEdit()

        self.show_vue = show_vue
        self.setup()

    def setup(self):
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        Layout = QFormLayout()
        # Add a label and a line edit to the form layout

        Layout.addRow("Last Name", self.last_name)

        Layout.addRow("Email", self.email)

        # Create a layout for the checkboxes
        ValidationLayout = QVBoxLayout()

        btn_add = QPushButton('Connexion', self)
        btn_add.clicked.connect(self.ConnectUser)
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

    def ConnectUser(self):
        # Show connexion formular
        data = {'lastname': self.last_name.text(),
                'email': self.email.text()}
        self.email = data['email']
        self.last_name = data['lastname']
        print(self.email, self.last_name)
        member = self._liste_controller.search_member_email(self.email, self.last_name)
        print(member)
        print('Bonjour', self.lastname, self.email, 'bienvenu sur votre compte')