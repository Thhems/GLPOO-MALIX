from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.liste import List
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class ListDAO(DAO):
    """
    List Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(List).filter_by(id=id).order_by(List.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(List).order_by(List.firstname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, firstname: str, lastname: str):
        try:
            return self._database_session.query(List).filter_by(firstname=firstname, lastname=lastname)\
                .order_by(List.firstname).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_email(self, email: str, lastname: str):
        try:
            return self._database_session.query(List).filter_by(email=email, lastname=lastname) \
                .order_by(List.email).one()
        except NoResultFound:
            raise ResourceNotFound()

    def createlist(self, data: dict):
        try:
            member = List(firstname=data.get('firstname'), lastname=data.get('lastname'), email=data.get('email'),
                        nb=data.get('nb'), type=data.get('type'))
            self._database_session.add(member)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Vous avez déjà été inscrit")
        
        return member

    def update(self, member: List, data: dict):
        if 'firstname' in data:
            member.firstname = data['firstname']
        if 'lastname' in data:
            member.lastname = data['lastname']
        if 'email' in data:
            member.email = data['email']
        if 'nb' in data:
            member.nb = data['nb']
        if 'type' in data:
            member.type = data['type']
        try:
            self._database_session.merge(member)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Erreur la donnée est peut-être malformée")
        return member

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
