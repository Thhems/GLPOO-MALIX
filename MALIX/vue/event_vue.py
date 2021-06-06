from vue.common import Common


class EventVue:
    """
    Event Vue
    Event interface features
    """

    def __init__(self, event_controller):
        self._common = Common()
        self._event_controller = event_controller

    def add_event(self):
        # Show subscription formular
        data = {}
        print("Ajout d'un évènement")
        print()
        data['name'] = self._common.ask_name(key_name="name")
        data['date'] = self._common.ask_date()
        data['places'] = self._common.ask_places()
        data['lieu'] = self._common.ask_lieu()
        data['prix'] = self._common.ask_prix()

        return self._event_controller.create_event(data)

    def show_event(self, event: dict):
        print("Détails de l'évènements: ")
        print(event['name'].capitalize())
        print("date:", event['date'])
        print("Nombre de places restantes:", event['places'])
        print("Lieu: ", event['lieu'])
        print("Prix: ", event['prix'])

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Succès de l'opération: %s" % message)

    def show_events(self):

        events = self._event_controller.list_events()

        print("Events: ")
        for event in events:
            print("* %s (%s) - %s places restantes - %s - %s euros" % (event['name'],
                                                             event['date'],
                                                             event['places'],
                                                             event['lieu'],
                                                             event['prix']))

    def search_event(self):
        name = self._common.ask_name('name')
        event = self._event_controller.search_event(name)
        return event

    def update_event(self):
        event = self.search_event()
        data = {}
        print("Mise à jour de l'évènement")
        print()
        data['name'] = self._common.ask_name(key_name="name", default=event['name'])
        data['date'] = self._common.ask_date()
        data['places'] = self._common.ask_places()
        data['lieu'] = self._common.ask_lieu()
        data['prix'] = self._common.ask_prix()
        print()
        return self._event_controller.update_event(event['id'], data)

    def resa_event(self, nom, nb):
        event = self._event_controller.search_event(nom)
        data = {}
        print("Mise à jour de l'évènement")
        event['places'] -= nb
        data['name'] = event['name']
        data['date'] = event['date']
        data['places'] = event['places']
        data['lieu'] = event['lieu']
        data['prix'] = event['prix']
        print("Vous avez réservé "+str(nb)+" places pour "+event['name'] + " pour " + str(event['prix']*nb)+" à "+event['lieu'] + " il reste "+ str(event['places']))
        return self._event_controller.update_event(event['id'], data)

    def delete_event(self):
        event = self.search_event()
        self._event_controller.delete_event(event['id'])
        self.succes_message()
