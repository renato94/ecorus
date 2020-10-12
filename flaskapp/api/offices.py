from flask import jsonify, make_response
from models import Office
from database import db_session
from flask import request
from api import bp


@bp.route('/offices', methods=['GET'])
def get_offices():
    offices = Office.query.all()
    office_info = [office.to_dict() for office in offices]
    return jsonify({'success': True, 'offices': office_info})


@bp.route('/offices/<id>', methods=['GET'])
def get_office(id):
    office = Office.query.get(id)
    office_info = office.to_dict() if office else "No office with that ID"
    return make_response(jsonify({'success': True, 'offices': office_info}))


@bp.route('/offices', methods=['POST'])
def create_office():
    json = request.json
    office = Office(json['name'])
    try:
        db_session.add(office)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    return jsonify({'success': success, 'office': office.to_dict()})


@bp.route('/offices', methods=['PUT'])
def update_office():
    office_id = request.args.get('id', None)
    office = Office.query.get(int(office_id))

    if not office and office_id:
        office = Office(name=request.json['name'])
    else:
        office.update(**request.get_json())
    try:
        db_session.add(office)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False

    return jsonify({'success': success, 'office': office.to_dict()})


@bp.route('/offices/<int:id>', methods=['DELETE'])
def delete_office(id):
    office = Office.query.get(id)
    try:
        db_session.delete(office)
        db_session.commit()
        success = True
    except:
        db_session.rollback()
        success = False
    return jsonify({'success': success})
