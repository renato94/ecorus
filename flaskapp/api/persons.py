from flask import jsonify, request
from models import Office, Person, PersonValidator
from database import db_session
from api.helpers import valid_api_request, bad_request
from api import bp


@bp.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return jsonify({'success': True, 'persons': [person.to_dict() for person in persons]})


@bp.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    person_info = person.to_dict() if person else "No person with that ID"
    return jsonify({'success': True, 'persons': person_info})


@bp.route('/persons/<int:id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)
    if not person:
        success, errors = valid_api_request(request, update_can_create=True)
        if not success:
            return bad_request(errors, 400)
        person = Person(name=request.json['name'], age=request.json['age'])
    else:
        person.update(**request.get_json())
    try:
        db_session.add(person)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    person_info = person.to_dict() if person else "No person with that ID"
    return jsonify({'success': success, 'persons': person_info})


@bp.route('/persons', methods=['POST'])
def create_person():
    json = request.json
    person = Person(json['name'], json['age'])
    try:
        db_session.add(person)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    return jsonify({'success': success, 'person': person.to_dict()})


@bp.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    person_id = id
    person = Person.query.get(int(person_id))
    try:
        db_session.delete(person)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    return jsonify({'success': success})


@bp.route('/persons/<int:id>/startworkingfor/<int:office_id>', methods=['GET'])
def start_working_for(id, office_id):
    errors = []
    office = Office.query.get(office_id)
    person = Person.query.get(id)
    if person and office:
        person.office_id = office_id
        office.start_working_for(person)
    else:
        errors.append(f'No person with id={id}' if not person else f'No office with id: {id}')
    try:
        db_session.add(person)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    return jsonify({'success': success, 'errors': errors})


@bp.route('/persons/<int:id>/finishworkingfor', methods=['GET'])
def finish_working_for(id):
    errors = []
    person = Person.query.get(id)
    if person:
        person.office_id = None
    else:
        errors.append(f'No person with id={id}')
    try:
        db_session.add(person)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    return jsonify({'success': success, 'errors': errors})
