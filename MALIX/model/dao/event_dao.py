from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.event import Event
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class EventDAO(DAO):
    """
    Event Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Event).filter_by(id=id).order_by(Event.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Event).order_by(Event.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str):
        try:
            return self._database_session.query(Event).filter_by(name=name)\
                .order_by(Event.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            event = Event(name=data.get('name'), date=data.get('date'), places=data.get('places'), lieu=data.get('lieu'), prix=data.get('prix'))
            self._database_session.add(event)
            self._database_session.flush()
        except IntegrityError:
            raise Error("event already exists")
        return event

    def update(self, event: Event, data: dict):
        if 'name' in data:
            event.name = data['name']
        if 'date' in data:
            event.date = data['date']
        if 'places' in data:
            event.places = data['places']
        if 'lieu' in data:
            event.places = data['lieu']
        if 'prix' in data:
            event.places = data['prix']
        try:
            self._database_session.merge(event)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return event

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
