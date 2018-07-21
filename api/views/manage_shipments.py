from flask import request, jsonify, make_response, Blueprint, g
from flask_restful import Resource
from api.models import Users, Pfi, Shipments
from api.helpers import token_required, validate_request
from api import db


statement_blueprint = Blueprint('statment', __name__)

@statement_blueprint.route('/api/v1/shipment', methods=['GET'])
@token_required
def get_all_shipments():
  """
  Returns all the registered statements
  """
  try:
    shipments = Shipments.query.all()
  except Exception:
    response_object = {
      'status': 'fail',
      'message': 'an error occured, try again'
    }
    return make_response(jsonify(response_object)), 500

  if shipments:
    result = []

    for count, values in enumerate(shipments):
      pfi = Pfi.query.filter_by(shipments_id=values.id).first()
      temp_pfi = dict(
        pfi_number=pfi.pfi_number,
        supplier_name=pfi.supplier_name
      )
      temp_result = dict(
        id=values.id,
        created_at=values.created_at,
        pfi=temp_pfi
      )
      result.append(temp_result)

    response_object = {
        'status': 'success',
        'data': result
      }
    return make_response(jsonify(response_object)), 200

  else:
    response_object = {
        'status': 'success',
        'data': []
      }
    return make_response(jsonify(response_object)), 200


@statement_blueprint.route('/api/v1/shipment/<shipment_id>', methods=['GET'])
@token_required
def get_single_shipment(shipment_id=None):
  """
  Get single shipment
  """
  try:
    if shipment_id:
      shipment = Shipments.query.filter_by(id=shipment_id).first()

      if shipment:
        pfi = Pfi.query.filter_by(shipments_id=shipment.id).first()
        pfi_result = dict(
          pfi_number=pfi.pfi_number,
          supplier_name=pfi.supplier_name
        )
        result = dict(
          id=shipment.id,
          created_at=shipment.created_at,
          pfi=pfi_result
        )

        resopnse_object = jsonify({
          'status': 'success',
          'data': result
        }), 200
        return resopnse_object
      else:
        resopnse_object = jsonify({
          'status': 'fail',
          'message': 'this shipment does not exist'
        }), 404
        return resopnse_object
    else:
      resopnse_object = jsonify({
          'status': 'fail',
          'message': 'pft_id is required'
        }), 400
      return resopnse_object
  except Exception as error:
    print(error)
    resopnse_object = jsonify({
      'status': 'fail',
      'message': 'Some error occured, please try again'
    }), 500
    return resopnse_object