from flask import request, jsonify, make_response, Blueprint, g
from flask_restful import Resource
from api.models import Shipments, RequiredPermission
from api.helpers import token_required, validate_request
from api import db


permissions_blueprint = Blueprint('permissions', __name__)

@permissions_blueprint.route('/api/v1/permissions', methods=['POST'])
@token_required
@validate_request((str, 'permission_name'))
@validate_request((int, 'shipments_id'))
def create_permission():
  """
  Create new permission
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
    new_permission = RequiredPermission(
      permission_name=post_data['permission_name'],
      shipments_id=post_data['shipments_id']
    )

    db.session.add(new_permission)
    db.session.commit()

    result = dict(
      permission_name=new_permission.permission_name,
      shipments_id=new_permission.shipments_id,
      gotten=new_permission.gotten
    )
    response_object = {
      'status': 'success',
      'data': result
    }
    return make_response(jsonify(response_object)), 201


@permissions_blueprint.route('/api/v1/permissions/<shipments_id>', methods=['GET'])
@token_required
def get_permissions(shipments_id=None):
  """
  Get all available permissions
  """
  if shipments_id is None:
    response_object = {
      'status': 'fail',
      'message': 'shipments_id is required'
    }
    return make_response(jsonify(response_object)), 404
  else:
    shipment = Shipments.query.filter_by(id=shipments_id).first()

    if shipment is None:
      response_object = {
        'status': 'fail',
        'message': 'this shipment does not exist'
      }
      return make_response(jsonify(response_object)), 404
    else:
      permissions = RequiredPermission.query.filter_by(shipments_id=shipments_id).all()

      if permissions:
        result = []

        for count, values in enumerate(permissions):
          temp_result = dict(
            permission_name=values.permission_name,
            id=values.id,
            gotten=values.gotten
          )

          result.append(temp_result)

      response_object = {
        'status': 'success',
        'data': result
      }
      return make_response(jsonify(response_object)), 200


@permissions_blueprint.route('/api/v1/permissions/<permission_id>', methods=['PUT'])
@token_required
@validate_request((str, 'permission_name', 'gotten'))
def update_permissions(permission_id=None):
  """
  Update a given permission
  """
  post_data = request.get_json()
  permission = RequiredPermission.query.filter_by(id=permission_id).first()

  if permission is None:
    response_object = {
      'status': 'fail',
      'message': 'this permission does not exist'
    }
    return make_response(jsonify(response_object)), 404
  else:
    permission.permission_name = post_data['permission_name']
    permission.gotten = bool(post_data['gotten'])

    db.session.add(permission)
    db.session.commit()

    result = dict(
      permission_name=permission.permission_name,
      shipments_id=permission.shipments_id,
      gotten=permission.gotten
    )
    response_object = {
      'status': 'success',
      'data': result
    }
    return make_response(jsonify(response_object)), 200