
from model.database import DatabaseEngine
from controller.member_controller import MemberController
from vue.member_vue import MemberVue


def main():
    print("Bienvenue sur Malix")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///shop.db')
    database_engine.create_database()
    member_controller = MemberController(database_engine)
    MemberVue(member_controller).member_shell()


if __name__ == "__main__":
    main()
