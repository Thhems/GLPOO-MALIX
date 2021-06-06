from vue.common import Common
from exceptions import ResourceNotFound, Error, InvalidData


class ListVue:
    """
    List Vue
    Lists interface features
    """

    def __init__(self, member_controller, list_controller):
        # EventVue.__init__(self, event_controller)
        self._common = Common()
        self._member_controller = member_controller
        self._list_controller = list_controller

    def add_list(self, artiste, nom, mail):
        data = {}
        data['firstname'] = artiste
        data['lastname'] = nom
        data['email'] = mail

        return self._list_controller.add_list(data)

    def create_list(self, artiste, nom, mail, nb):
        data = {}
        data['firstname'] = artiste
        data['lastname'] = nom
        data['email'] = mail
        data['nb'] = nb
        data['type'] = 'customer'
        return self._list_controller.create_list(data)

    def show_list(self, member: dict):
        print("Profile de l'inscrit: ")
        print("Event :"+member['firstname'].capitalize())
        print(member['lastname'].capitalize())
        print("email:", member['email'])
        print("Nombre de places:", member['nb'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Succès de l'opération: %s" % message)

    def show_lists(self):

        members = self._list_controller.listall()

        print("Clients: ")
        for member in members:
            print("* %s || %s (%s) - %s places" % (member['firstname'].capitalize(),
                                         member['lastname'].capitalize(),
                                         member['email'],
                                         member['nb']))

    def show_inscription(self):

        members = self._list_controller.list()

        print("Inscrits: ")
        for member in members:
            print(
                "* %s | %s (%s) %s" % (member['firstname'].capitalize(), member['lastname'].capitalize(),
                                       member['email'], member['nb']))

    def search_member(self):
        firstname = self._common.ask_name('firstname')
        lastname = self._common.ask_name('lastname')
        member = self._member_controller.search_member(firstname, lastname)
        return member

    def update_member(self):
        member = self.search_member()
        data = {}
        print("Mise à jour de la réservation")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname", default=member['firstname'])
        data['lastname'] = self._common.ask_name(key_name="lastname", default=member['lastname'])
        data['email'] = self._common.ask_email(default=member['email'])
        data['nb'] = self._common.ask_nb(default=member['nb'])
        data['type'] = self._common.ask_type(default=member['type'])
        print()
        return self._member_controller.update_member(member['id'], data)

    def remove_member(self):
        member = self.search_member()
        self._member_controller.remove_member(member['id'])
        self.succes_message()

    def help_member(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

