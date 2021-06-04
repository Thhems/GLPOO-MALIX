from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint, Float


class List(Base):
    __tablename__ = 'list'
    __table_args__ = (UniqueConstraint('firstname', 'lastname', 'email', 'nb'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(256), nullable=False)
    nb = Column(Float(), nullable=False)
    type = Column(String(10), nullable=False)

    def __repr__(self):
        return "<Inscrit (%s %s %s %s)>" % (self.firstname, self.lastname.upper(), self.type, self.nb)

    def to_dictliste(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "nb": self.nb,
            "type": self.type
        }
