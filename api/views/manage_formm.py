from flask import request, jsonify, make_response, Blueprint, g
from flask_restful import Resource
from api.models import Formm, LetterOfCredit, Insurance, Shipments
from api.helpers import token_required, validate_request
from api import db


formm_blueprint = Blueprint('formm', __name__)

@formm_blueprint.route('/api/v1/formm/<shipment_id>', methods=['GET'])
@token_required
def get_single_formm(shipment_id=None):
  """
  Get a single formm
  """
  if shipment_id:
    shipment = Shipments.query.filter_by(id=shipment_id).first()

    if shipment is None:
      response_object = {
        'status': 'fail',
        'message': 'This shipment does not exist'
      }
      return make_response(jsonify(response_object)), 404
    else:
      formm = Formm.query.filter_by(shipments_id=shipment_id).first()

      if formm is None:
        response_object = {
          'status': 'fail',
          'message': 'This Form M does not exist'
        }
        return make_response(jsonify(response_object)), 404
      else:
        letterofcredit = LetterOfCredit.query.filter_by(formm_id=formm.id).first()

        if letterofcredit is None:
          insurance = Insurance.query.filter_by(formm_id=formm.id).first()

          if insurance is None:
            result = dict(
              id=formm.id,
              formm_number=formm.formm_number,
              insurance={},
              letterofcredit={}
            )
            response_object = {
              'status': 'success',
              'data': result
            }
            return make_response(jsonify(response_object)), 200
          else:
            result = dict(
              id=formm.id,
              formm_number=formm.formm_number,
              insurance=insurance,
              letterofcredit={}
            )
            response_object = {
              'status': 'success',
              'data': result
            }
            return make_response(jsonify(response_object)), 200
        else:
          letterofcredit = LetterOfCredit.query.filter_by(formm_id=formm.id).first()

          if letterofcredit is None:
            insurance = Insurance.query.filter_by(formm_id=formm.id).first()

            if insurance is None:
              result = dict(
                id=formm.id,
                formm_number=formm.formm_number,
                insurance={},
                letterofcredit=letterofcredit
              )
              response_object = {
                'status': 'success',
                'data': result
              }
              return make_response(jsonify(response_object)), 200
            else:
              result = dict(
                id=formm.id,
                formm_number=formm.formm_number,
                insurance=insurance,
                letterofcredit=letterofcredit
              )
              response_object = {
                'status': 'success',
                'data': result
              }
              return make_response(jsonify(response_object)), 200
  else:
    response_object = {
      'status': 'fail',
      'message': 'shipment_id is required'
    }
    return make_response(jsonify(response_object)), 400


@formm_blueprint.route('/api/v1/formm', methods=['POST'])
@token_required
@validate_request((int, 'shipments_id', 'formm_number'))
def create_formm():
  """
  Create a Formm
  """
  post_data = request.get_json()

  shipment = Shipments.query.filter_by(id=post_data['shipments_id']).first()

  if shipment is None:
    response_object = {
      'status': 'fail',
      'message': 'this shipment does not exist'
    }
    return make_response(jsonify(response_object)), 404
  else:
    formm = Formm.query.filter_by(formm_number=post_data['formm_number']).first()

    if formm:
      response_object = {
        'status': 'fail',
        'message': 'a formm_number already exists for this shipment'
      }
      return make_response(jsonify(response_object)), 400
    else:
      formm = Formm.query.filter_by(shipments_id=post_data['shipments_id']).first()
      
      if formm:
        response_object = {
          'status': 'fail',
          'message': 'a Form M already exists for this shipment'
        }
        return make_response(jsonify(response_object)), 400
      else:
        new_formm = Formm(
          shipments_id=post_data['shipments_id'],
          formm_number=post_data['formm_number']
        )
        db.session.add(new_formm)
        db.session.commit()

        result = dict(
          id=new_formm.id,
          formm_number=new_formm.formm_number,
          shipments_id=new_formm.shipments_id
        )

        response_object = {
          'status': 'success',
          'data': result
        }

        return make_response(jsonify(response_object)), 201


@formm_blueprint.route('/api/v1/formm/<formm_id>', methods=['PUT'])
@token_required
@validate_request((int, 'shipments_id', 'formm_number'))
def update_formm(formm_id=None):
  """
  Update a formm
  """
  if formm_id is None:
    response_object = {
      'status': 'fail',
      'message': 'Formm_id is required'
    }
    return make_response(jsonify(response_object)), 400
  else:
    post_data = request.get_json()
    formm = Formm.query.filter_by(id=formm_id).first()

    if formm is None:
      response_object = {
        'status': 'fail',
        'message': 'This Form M does not exist'
      }
      return make_response(jsonify(response_object)), 404

    formm.formm_number = post_data['formm_number']

    db.session.add(formm)
    db.session.commit()

    result = dict(
      id=formm.id,
      formm_number=formm.formm_number,
      shipments_id=formm.shipments_id
    )

    response_object = {
      'status': 'success',
      'data': result
    }

    return make_response(jsonify(response_object)), 200