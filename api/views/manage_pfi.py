from flask import request, jsonify, make_response, Blueprint, g
from flask_restful import Resource
from api.models import Users, Pfi, Shipments
from api.helpers import token_required, validate_request
from api import db


pfi_blueprint = Blueprint('pfi', __name__)

@pfi_blueprint.route('/api/v1/pfi', methods=['POST'])
@token_required
@validate_request(((str, 'item_detail', 'type', 'url', 'supplier_name')))
@validate_request(((int, 'quantity', 'cost', 'hs_code', 'pfi_number', 'hscode_percentage', 'unit_cost')))
def create_pfi():
  """
  Controls the pfi login operations
  """
  post_data = request.get_json()
  shipment = Shipments(
    user_id = g.current_user.user_id
  )

  db.session.add(shipment)
  db.session.commit()

  pft = Pfi(
    quantity = post_data['quantity'],
    cost = post_data['cost'],
    hs_code = post_data['hs_code'],
    items_detail = post_data['item_detail'],
    pfi_type = post_data['type'],
    url = post_data['url'],
    shipments_id = shipment.id,
    supplier_name = post_data['supplier_name'],
    pfi_number = post_data['pfi_number'],
    hscode_percentage = post_data['hscode_percentage'],
    unit_cost = post_data['unit_cost']
  )

  db.session.add(pft)
  db.session.commit()

  new_pfi = dict(
    id=pft.id,
    quantity=pft.quantity,
    cost=pft.cost,
    hs_code=pft.hs_code,
    items_detail=pft.items_detail,
    pft_type=pft.pfi_type,
    url=pft.url,
    shipment_id=pft.shipments_id,
    supplier_name=pft.supplier_name,
    pfi_number=pft.pfi_number,
    hscode_percentage=pft.hscode_percentage,
    unit_cost=pft.unit_cost
  )

  resopnse_object = {
    'status': 'success',
    'message': 'successfully created pfi',
    'data': new_pfi
  }
  return make_response(jsonify(resopnse_object)), 200


@pfi_blueprint.route('/api/v1/pfi/<pfi_id>', methods=['GET'])
@token_required
def get_single_pfi(pfi_id=None):
  """
  Get a single pfi
  """
  try:
    if pfi_id:
      pfi = Pfi.query.filter_by(id=pfi_id).first()

      if pfi:
        queried_pfi = dict(
          id=pfi.id,
          quantity=pfi.quantity,
          cost=pfi.cost,
          hs_code=pfi.hs_code,
          items_detail=pfi.items_detail,
          pft_type=pfi.pfi_type,
          url=pfi.url,
          shipment_id=pfi.shipments_id,
          supplier_name=pfi.supplier_name,
          pfi_number=pfi.pfi_number,
          hscode_percentage=pfi.hscode_percentage,
          unit_cost=pfi.unit_cost
        )
        resopnse_object = jsonify({
          'status': 'success',
          'data': queried_pfi
        }), 200
        return resopnse_object
      else:
        resopnse_object = jsonify({
          'status': 'fail',
          'message': 'this pft document does not exist'
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


@pfi_blueprint.route('/api/v1/pfi/<pfi_id>', methods=['PUT'])
@token_required
@validate_request(((str, 'item_detail', 'type', 'url', 'supplier_name')))
@validate_request(((int, 'quantity', 'cost', 'hs_code', 'pfi_number', 'hscode_percentage', 'unit_cost')))
def update_pfi(pfi_id=None):
  """
  Controls the pfi login operations
  """
  post_data = request.get_json()

  try:
    if pfi_id:
      pfi = Pfi.query.filter_by(id=pfi_id).first()

      if pfi:

        pfi.quantity = post_data['quantity']
        pfi.cost = post_data['cost']
        pfi.hs_code = post_data['hs_code']
        pfi.items_detail = post_data['item_detail']
        pfi.pfi_type = post_data['type']
        pfi.url = post_data['url']
        pfi.supplier_name = post_data['supplier_name']
        pfi.pfi_number = post_data['pfi_number']
        pfi.hscode_percentage = post_data['hscode_percentage']
        pfi.unit_cost = post_data['unit_cost']

        db.session.add(pfi)
        db.session.commit()

        updated_pfi = dict(
          id= pfi.id,
          quantity=pfi.quantity,
          cost=pfi.cost,
          hs_code=pfi.hs_code,
          items_detail=pfi.items_detail,
          pfi_type=pfi.pfi_type,
          url=pfi.url,
          shipment_id=pfi.shipments_id,
          supplier_name=pfi.supplier_name,
          pfi_number=pfi.pfi_number,
          hscode_percentage=pfi.hscode_percentage,
          unit_cost=pfi.unit_cost
        )
        
        resopnse_object = {
          'status': 'success',
          'message': 'successfully updated pfi',
          'data': updated_pfi
        }
        return make_response(jsonify(resopnse_object)), 200
      else:
        resopnse_object = jsonify({
          'status': 'fail',
          'message': 'this pfi document does not exist'
        }), 404
        return resopnse_object
    else:
      resopnse_object = jsonify({
          'status': 'fail',
          'message': 'pfi_id is required'
        }), 400
      return resopnse_object
  except Exception as error:
    print(error)
    resopnse_object = jsonify({
      'status': 'fail',
      'message': 'Some error occured, please try again'
    }), 500
    return resopnse_object
