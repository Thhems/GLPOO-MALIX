from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint, Float


class Event(Base):
    __tablename__ = 'event'
    __table_args__ = (UniqueConstraint('name', 'date', 'places'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    name = Column(String(50), nullable=False)
    date = Column(String(50), nullable=False)
    places = Column(Float(), nullable=False)

    def __repr__(self):
        return "<Event (%s %s %s)>" % (self.name, self.date, self.places)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "places": self.places,
        }
