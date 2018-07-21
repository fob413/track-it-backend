from flask import request, jsonify, make_response, Blueprint
from flask_restful import Resource
from api.models.users import Users

login_blueprint = Blueprint('login', __name__)
logout_blueprint = Blueprint('logout', __name__)

@login_blueprint.route('/api/v1/login', methods=['POST'])
def user_login():
    """
    Controls the login operations
    """
    post_data = request.get_json()
    try:
        user = Users.query.filter_by(email=post_data.get('email')).first()
        if user is not None and user.verify_password(post_data.get('password')):
            auth_token = user.encode_auth_token(user.id)
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(response_object)), 200
        else:
            return make_response(jsonify({
                'status': 'fail',
                'message': 'wrong email or password'
            })), 401
    except Exception as error:
        return make_response(jsonify({
            'status': 'fail',
            'message': 'An error occured'
        })), 500