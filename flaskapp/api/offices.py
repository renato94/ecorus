from flask import jsonify, make_response
from flaskapp.models import Office
from flaskapp.database import db_session, save_object, delete_object
from flask import request
from flaskapp.api import bp_api


@bp_api.route('/offices', methods=['GET'])
def get_offices():
    offices = Office.query.all()
    office_info = [office.to_dict() for office in offices]
    return jsonify({'success': True, 'offices': office_info})


@bp_api.route('/offices/<int:id>', methods=['GET'])
def get_office(id):
    office = Office.query.get(id)
    office_info = office.to_dict() if office else "No office with that ID"
    return make_response(jsonify({'success': True, 'offices': office_info}))


@bp_api.route('/offices', methods=['POST'])
def create_office():
    json = request.json
    office = Office(json['name'])
    success, errors = save_object(office)

    return jsonify({'success': success, 'office': office.to_dict()})


@bp_api.route('/offices/<int:id>', methods=['PUT'])
def update_office(id):
    office = Office.query.get(int(id))

    if not office:
        office = Office(name=request.json['name'])
    else:
        office.update(**request.get_json())
    success, errors = save_object(office)
    return jsonify({'success': success, 'office': office.to_dict()})


@bp_api.route('/offices/<int:id>', methods=['DELETE'])
def delete_office(id):
    office = Office.query.get(id)
    success, errors = delete_object(office)
    return jsonify({'success': success})
