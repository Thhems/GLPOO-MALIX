
from controller.member_controller import MemberController
from controller.event_controller import EventController
from model.database import DatabaseEngine
from vue.admin_vue import AdminVue


def main():
    print("Welcome to MALIX")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    database_event = DatabaseEngine(url='sqlite:///shop.db')
    database_event.create_database()
    admin_controller = MemberController(database_engine)
    event_controller = EventController(database_event)
    AdminVue(admin_controller, event_controller).admin_shell()


if __name__ == "__main__":
    main()
