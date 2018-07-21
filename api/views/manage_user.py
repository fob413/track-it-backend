from flask import request, jsonify, make_response, Blueprint
from flask_login import login_required, login_user, logout_user
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
    user = Users.query.filter_by(email=post_data.get('email')).first()
    if user is not None and user.verify_password(post_data.get('password')):
        login_user(user)
        response_object = {
            'status': 'success',
            'message': f'Login was successful for {user.email}'
        }
        return make_response(jsonify(response_object)), 200
    return make_response(jsonify({
        'status': 'fail',
        'message': 'wrong email or password'
    })), 401


@logout_blueprint.route('/api/v1/logout', methods=['POST'])
@login_required
def user_logout():
    """
    Controls the logout operations
    """
    try:
        logout_user()
        return make_response(jsonify({
            'status': 'success',
            'message': 'logout successful'
        })), 200
    except Exception as error:
        print(error)
        return make_response(jsonify({
            'status': 'fail',
            'message': 'oops, something went wrong'
        })), 500
