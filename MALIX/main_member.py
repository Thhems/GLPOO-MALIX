
from model.database import DatabaseEngine
from controller.member_controller import MemberController
from exceptions import Error
from vue.member_vue import MemberVue


def main():
    print("Bienvenue sur Malix")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    member_controller = MemberController(database_engine)
    member_vue = MemberVue(member_controller).member_shell()

    try:
        member = member_vue.add_member("customer") #add_member = question crea compte
        member_vue.show_member(member)
    except Error as e:
        member_vue.error_message(str(e))


if __name__ == "__main__":
    main()
