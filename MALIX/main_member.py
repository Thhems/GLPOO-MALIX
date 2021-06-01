
from model.database import DatabaseEngine
from controller.member_controller import MemberController
from controller.event_controller import EventController
from exceptions import Error
from vue.member_vue import MemberVue


def main():
    print("Bienvenue sur Malix")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    database_event = DatabaseEngine(url='sqlite:///shop.db')
    database_event.create_database()
    member_controller = MemberController(database_engine)
    event_controller = EventController(database_event)
    member_vue = MemberVue(member_controller, event_controller).member_shell()


if __name__ == "__main__":
    main()
