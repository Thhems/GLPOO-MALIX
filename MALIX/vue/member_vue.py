from vue.common import Common
from exceptions import ResourceNotFound, Error, InvalidData
from vue.event_vue import EventVue
from vue.liste_vue import ListVue


class MemberVue(EventVue):
    """
    Member Vue
    Members interface features
    """
    def __init__(self, member_controller, event_controller, list_controller):
        EventVue.__init__(self, event_controller)
        # ListVue.__init__(self, list_controller)
        self._common = Common()
        self._member_controller = member_controller
        self._list_controller = list_controller

    def add_member(self, user_type):
        # Show subscription formular
        data = {}
        print("Inscription du client")
        # print(user_type)
        print()
        data['firstname'] = self._common.ask_name(key_name="firstname")
        data['lastname'] = self._common.ask_name(key_name="lastname")
        data['email'] = self._common.ask_email()

        if user_type != 'customer':
            data['type'] = self._common.ask_type()
        else:
            data['type'] = user_type
        print('data', data)
        return self._member_controller.add_member(data)

    def connexion_member(self, user_type):
        data = {}
        print("Connexion")

        email = self._common.ask_name('email')
        lastname = self._common.ask_name('lastname')

        member = self._member_controller.search_member_email(email, lastname)
        return member

    def create_member(self, user_type):
        # Show subscription formular
        data = {}
        print("Inscription d'un client :")
        data['firstname'] = self._common.ask_name(key_name="firstname")
        data['lastname'] = self._common.ask_name(key_name="lastname")
        data['email'] = self._common.ask_email()
        data['type'] = 'customer'
        return self._member_controller.create_member(data)

    def show_member(self, member: dict):
        print("Profile du client: ")
        print(member['firstname'].capitalize(), member['lastname'].capitalize())
        print("email:", member['email'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_members(self):

        members = self._member_controller.list_members()

        print("Clients: ")
        for member in members:
            print("* %s %s (%s)" % (member['firstname'].capitalize(),
                                         member['lastname'].capitalize(),
                                         member['email']))

    def search_member(self):
        firstname = self._common.ask_name('firstname')
        lastname = self._common.ask_name('lastname')
        member = self._member_controller.search_member(firstname, lastname)
        return member

    def update_member(self):
        member = self.search_member()
        data = {}
        print("Update client")
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

        data = {}
        data['firstname'] = nom
        data['lastname'] = membre['lastname']
        data['email'] = membre['email']
        data['nb'] = nb
        data['type'] = 'customer'
        self._list_controller.create_list(data)
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
                                commands_inscr = {
                                    "retour": "retour au menu",
                                    "inscription": 'S\'inscrire à un autre événement',
                                    "help": "Montrer l'aide"
                                }
                                self.help_member(commands_inscr)
                                while True:
                                    try:
                                        command = self.ask_command(commands_inscr)
                                        if command == 'retour':
                                            break
                                        if command == 'help':
                                            self.help_member(commands_inscr)
                                        if command == 'inscription':
                                            self.ask_resa(member)
                                    except ResourceNotFound:
                                        self.error_message("Member not found")
                                    except InvalidData as e:
                                        self.error_message(str(e))
                                    except Error as e:
                                        self.error_message("An error occurred (%s)" % str(e))
                                self.help_member(commands_connecte)
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
