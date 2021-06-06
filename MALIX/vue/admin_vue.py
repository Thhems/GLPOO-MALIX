
import sys
from vue.member_vue import MemberVue
from vue.event_vue import EventVue
from vue.liste_vue import ListVue
from exceptions import ResourceNotFound, Error, InvalidData


class AdminVue(MemberVue, EventVue, ListVue):
    """
    Admin Vue
    Admin specific interfaces
    """

    def __init__(self, member_controller, event_controller, list_controller):
        MemberVue.__init__(self, member_controller, event_controller, list_controller)
        EventVue.__init__(self, event_controller)
        ListVue.__init__(self, member_controller, list_controller)
        # self._list_controller = list_controller

    def help(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('commande > ').lower().strip()
        while command not in commands.keys():
            print("Commande inconnue")
            command = input('commande >').lower().strip()

        return command

    def admin_shell(self):

        commands = {
            "quitter": "Quitter",
            "ajoutclient": "Ajouter un client",
            "listclient": "Lister les clients",
            "client": "Afficher le profile d'un client",
            "supprclient": "Supprimer un client",
            "majclient": "Mettre à jour un client",
            "ajoutevent": "Ajouter un évènement",
            "listevent": "Lister les évènements",
            "event": "Afficher un évènement",
            "supprevent": "Supprimer un évènement",
            "majevent": "Mettre à jour un évènement",
            "list": "Lister les personnes inscrites",
            "supprinscrit": "supprimer un client inscrit",
            "aide": "Afficher l'aide"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'quitter':
                    break
                elif command == 'ajoutclient':
                    user_type = 'unknown'
                    member = self.create_member(user_type)
                    self.show_member(member)
                elif command == 'listclient':
                    self.show_members()
                elif command == 'client':
                    member = self.search_member()
                    self.show_member(member)
                elif command == 'supprclient':
                    self.delete_member()
                elif command == 'majclient':
                    member = self.update_member()
                    self.show_member(member)
                elif command == 'ajoutevent':
                    event = self.add_event()
                    self.show_event(event)
                elif command == 'listevent':
                    self.show_events()
                elif command == 'event':
                    event = self.search_event()
                    self.show_event(event)
                elif command == 'supprevent':
                    self.delete_event()
                elif command == 'majevent':
                    event = self.update_event()
                    self.show_event(event)
                elif command == 'list':
                    self.show_lists()
                elif command == 'aide':
                    self.help(commands)
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))