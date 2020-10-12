from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from flaskapp.models import Office, Person
from flaskapp.database import db_session, save_object, delete_object
from flaskapp.api import bp_api


@bp_api.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify({'success': True, 'persons': [person.to_dict() for person in persons]})


@bp_api.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    person_info = person.to_dict() if person else "No person with that ID"
    return jsonify({'success': True, 'persons': person_info})


@bp_api.route('/persons/<int:id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)
    person.update(**request.get_json())
    person_info = person.to_dict() if person else "No person with that ID"
    success, errors = save_object(person)
    return jsonify({'success': success, 'person': person_info, 'errors': errors})


@bp_api.route('/persons', methods=['POST'])
def create_person():
    json = request.json
    person = Person(json['name'], json['age'])
    success, errors = save_object(person)
    return jsonify({'success': success, 'person': person.to_dict()})


@bp_api.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    success, errors = delete_object(person)
    return jsonify({'success': success})


@bp_api.route('/persons/<int:id>/startworkingfor/<int:office_id>', methods=['GET'])
def start_working_for(id, office_id):
    errors = []
    office = Office.query.get(office_id)
    person = Person.query.get(id)
    if person and office:
        person.office_id = office_id
        office.start_working_for(person)
    else:
        errors.append(f'No person with id={id}' if not person else f'No office with id: {id}')
    success, errors = save_object(person)
    return jsonify({'success': success, 'errors': errors})


@bp_api.route('/persons/<int:id>/finishworkingfor', methods=['GET'])
def finish_working_for(id):
    errors = []
    person = Person.query.get(id)
    if person:
        success, errors = save_object(person)
    else:
        errors.append(f'No person with id={id}')
    return jsonify({'success': success, 'errors': errors})
