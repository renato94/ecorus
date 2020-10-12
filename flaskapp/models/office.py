from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flaskapp.database import Base


class OfficeValidator(object):
    create_schema = {'name': {'required': True, 'type': 'string', 'minlength': 1, 'maxlength': 50}}
    update_schema = {'name': {'required': False, 'type': 'string', 'minlength': 1, 'maxlength': 50}}


class Office(Base):
    __tablename__ = 'offices'

    __id = Column('id', Integer, primary_key=True)
    __name = Column('name', String(50))
    __people_working = relationship('Person', backref='office')

    def __init__(self, name):
        self.name = name
        self.people_working = []

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def people_working(self):
        return self.__people_working

    @property
    def people_working_names(self):
        return ','.join([person.name for person in self.people_working])

    @people_working.setter
    def people_working(self, new_people_working):
        self.__people_working = new_people_working

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def start_working_for(self, new_person):
        updated_people_working = self.people_working
        updated_people_working.append(new_person)
        self.people_working = updated_people_working
        return True

    def finished_working_for(self, old_person):
        if old_person in self.people_working:
            updated_people_working = self.people_working
            updated_people_working.remove(old_person)
            self.people_working = updated_people_working
            return True
        return False

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'people_working': [person.to_dict() for person in self.people_working if person]
        }

    def __repr__(self):
        return 'Office: <name:{0}><people_working:{1}>'.format(self.name, self.people_working)
