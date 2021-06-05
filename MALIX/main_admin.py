
from controller.member_controller import MemberController
from controller.event_controller import EventController
from controller.liste_controller import ListController
from model.database import DatabaseEngine
from vue.admin_vue import AdminVue


def main():
    print("Bienvenue sur MALIX")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    database_event = DatabaseEngine(url='sqlite:///shop.db')
    database_event.create_database()
    database_resa = DatabaseEngine(url='sqlite:///shop.db')
    database_resa.create_database()
    admin_controller = MemberController(database_engine)
    event_controller = EventController(database_event)
    resa_controller = ListController(database_resa)
    AdminVue(admin_controller, event_controller, resa_controller).admin_shell()


if __name__ == "__main__":
    main()
