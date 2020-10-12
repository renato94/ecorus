from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class PersonValidator(object):
    create_schema = {'name': {'required': True, 'type': 'string', 'minlength': 1, 'maxlength': 50},
                     'age': {'required': True, 'type': 'integer', 'min': 0, 'max': 100}}
    update_schema = {'name': {'required': False, 'type': 'string', 'minlength': 1, 'maxlength': 50},
                     'age': {'required': False, 'type': 'integer', 'min': 0, 'max': 100}}


class Person(Base):
    __tablename__ = 'persons'

    __id = Column('id', Integer, primary_key=True)
    __name = Column('name', String(50))
    __age = Column('age', Integer)
    __office_id = Column('office_id', Integer, ForeignKey('offices.id'))

    def __init__(self, name, age=25):
        self.name = name
        self.age = age

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
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def office_id(self):
        return self.__office_id

    @property
    def office(self):
        return self.office

    @office_id.setter
    def office_id(self, new_office_id):
        self.__office_id = new_office_id

    def happy_birthday(self):
        self.age = self.age + 1

    def change_name(self, new_name):
        self.name = new_name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __repr__(self):
        return 'Person: <name:{0}><age:{1}>'.format(self.name, self.age)
