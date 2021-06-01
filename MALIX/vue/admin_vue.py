
import sys
from vue.member_vue import MemberVue
from vue.event_vue import EventVue
from exceptions import ResourceNotFound, Error, InvalidData


class AdminVue(MemberVue, EventVue):
    """
    Admin Vue
    Admin specific interfaces
    """

    def __init__(self, member_controller, event_controller):
        MemberVue.__init__(self, member_controller)
        EventVue.__init__(self, event_controller)

    def help(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('command > ').lower().strip()
        while command not in commands.keys():
            print("Unknown command")
            command = input('command >').lower().strip()

        return command

    def admin_shell(self):

        commands = {
            "quitter": "Quitter",
            "addclient": "Ajouter un client",
            "listclient": "Lister les clients",
            "client": "Afficher le profile d'un client",
            "deleteclient": "Supprimer un client",
            "majclient": "Mettre à jour un client",
            "addevent": "Ajouter un évènement",
            "listevent": "Lister les évènements",
            "event": "Afficher un évènement",
            "deletevent": "Supprimer un évènement",
            "majevent": "Mettre à jour un évènement",
            "help": "Afficher l'aide"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'quitter':
                    break
                elif command == 'addclient':
                    user_type = 'unknown'
                    member = self.add_member(user_type)
                    self.show_member(member)
                elif command == 'listclient':
                    self.show_members()
                elif command == 'client':
                    member = self.search_member()
                    self.show_member(member)
                elif command == 'deleteclient':
                    self.delete_member()
                elif command == 'majclient':
                    member = self.update_member()
                    self.show_member(member)
                elif command == 'addevent':
                    event = self.add_event()
                    self.show_event(event)
                elif command == 'listevent':
                    self.show_events()
                elif command == 'event':
                    event = self.search_event()
                    self.show_event(event)
                elif command == 'deletevent':
                    self.delete_event()
                elif command == 'majevent':
                    event = self.update_event()
                    self.show_event(event)
                elif command == 'help':
                    self.help(commands)
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
