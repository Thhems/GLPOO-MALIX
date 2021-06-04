from vue.common import Common
from exceptions import ResourceNotFound, Error, InvalidData
from vue.event_vue import EventVue


class ListVue(EventVue):
    """
    List Vue
    Lists interface features
    """

    def __init__(self, member_controller, event_controller, list_controller):
        EventVue.__init__(self, event_controller)
        self._common = Common()
        self._member_controller = member_controller
        self._list_controller = list_controller

    def add_list(self, artiste, nom, mail):
        data = {}
        data['firstname'] = artiste
        data['lastname'] = nom
        data['email'] = mail

        return self._list_controller.add_list(data)

    def create_list(self, artiste, nom, mail):
        data = {}
        data['firstname'] = artiste
        data['lastname'] = nom
        data['email'] = mail
        data['type'] = 'customer'
        return self._list_controller.create_list(data)

    def show_list(self, member: dict):
        print("Profile de l'inscrit: ")
        print("Event :"+member['firstname'].capitalize())
        print(member['lastname'].capitalize())
        print("email:", member['email'])
        print("type:", member['type'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_lists(self):

        members = self._member_controller.list_members()

        print("Clients: ")
        for member in members:
            print("* %s || %s (%s) - %s" % (member['firstname'].capitalize(),
                                         member['lastname'].capitalize(),
                                         member['email'],
                                         member['type']))

    def show_inscription(self):

        members = self._list_controller.list_members()

        print("Inscrits: ")
        for member in members:
            print(
                "* %s | %s (%s)" % (member['firstname'].capitalize(), member['lastname'].capitalize(), member['email']))

    def search_member(self):
        firstname = self._common.ask_name('firstname')
        lastname = self._common.ask_name('lastname')
        member = self._member_controller.search_member(firstname, lastname)
        return member

    def update_member(self):
        member = self.search_member()
        data = {}
        print("Update réservation")
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname", default=member['firstname'])
        data['lastname'] = self._common.ask_name(key_name="lastname", default=member['lastname'])
        data['email'] = self._common.ask_email(default=member['email'])
        data['type'] = self._common.ask_type(default=member['type'])
        print()
        return self._member_controller.update_member(member['id'], data)

    def delete_member(self):
        member = self.search_member()
        self._member_controller.delete_member(member['id'])
        self.succes_message()

    def help_member(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('command > ').lower().strip()
        while command not in commands.keys():
            print("Commande inconnue")
            command = input('command >').lower().strip()

        return command

    def ask_resa(self, membre):
        print("A quel évènement voulez-vous vous incrire?")
        self.show_events()
        events = self._event_controller.list_events()
        nom = input('Nom de l évènement > ')
        good = 0
        while good == 0:
            for event in events:
                if nom == event['name']:
                    good = 1
            if good == 0:
                print("Cet evenement n'existe pas")
                nom = input('Nom de l évènement > ')
        nb = float(input('Nombre de places > '))
        while nb < 1 or nb > 11:
            nb = float(input('Nombre de places > '))
        for i in range(0, int(nb)):
            self.create_list(nom, membre['firstname'], membre['email'])
        self.resa_event(nom, nb)

    def member_shell(self):

        commands = {
            "exit": "Partir du Shell Shell",
            "creer": "Creer un compte",
            "connexion": "Connectez-vous",
            "event": "Afficher les évènements",
            "help": "Afficher cette aide"
        }

        self.help_member(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'creer':
                    user_type = 'unknown'
                    member = self.create_member(user_type)
                    self.show_member(member)
                elif command == 'connexion':
                    user_type = 'customer'
                    member = self.connexion_member(user_type)
                    self.show_member(member)
                    commands_connecte = {
                        "inscription": "S'inscrire à un évènement",
                        "deconnexion": "déconnectez-vous",
                        "help": "Montrer l'aide"
                    }
                    self.help_member(commands_connecte)
                    while True:
                        try:
                            command = self.ask_command(commands_connecte)
                            if command == 'inscription':
                                self.ask_resa(member)
                            elif command == 'deconnexion':
                                break
                            elif command == 'help':
                                self.help_member(commands_connecte)
                            else:
                                print("Commande inconnue")
                        except ResourceNotFound:
                            self.error_message("Member not found")
                        except InvalidData as e:
                            self.error_message(str(e))
                        except Error as e:
                            self.error_message("An error occurred (%s)" % str(e))
                    self.help_member(commands)
                elif command == 'event':
                    self.show_events()
                elif command == 'help':
                    self.help_member(commands)
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
