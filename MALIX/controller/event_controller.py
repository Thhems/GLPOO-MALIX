import re

from model.dao.event_dao import EventDAO
from exceptions import Error, InvalidData


class EventController:
    """
    Event actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_events(self):
        with self._database_engine.new_session() as session:
            events = EventDAO(session).get_all()
            events_data = [event.to_dict() for event in events]
        return events_data

    def get_event(self, event_id):
        with self._database_engine.new_session() as session:
            event = EventDAO(session).get(event_id)
            event_data = event.to_dict()
        return event_data

    def create_event(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save event in database
                event = EventDAO(session).create(data)
                event_data = event.to_dict()
                return event_data
        except Error as e:
            # log error
            raise e

    def update_event(self, event_id, event_data):

        self._check_profile_data(event_data, update=True)
        with self._database_engine.new_session() as session:
            event_dao = EventDAO(session)
            event = event_dao.get(event_id)
            event = event_dao.update(event, event_data)
            return event.to_dict()

    def delete_event(self, event_id):

        with self._database_engine.new_session() as session:
            event_dao = EventDAO(session)
            event = event_dao.get(event_id)
            event_dao.delete(event)

    def search_event(self, name):

        # Query database
        with self._database_engine.new_session() as session:
            event_dao = EventDAO(session)
            event = event_dao.get_by_name(name)
            return event.to_dict()

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        mandatories = {
            'name': {"type": str, "regex": name_pattern},
            'date': {"type": str},
            'places': {"type": float},
            'lieu': {"type": str},
            'prix': {"type": float},
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)
