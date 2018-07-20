from flask import request, jsonify, make_response
from flask_login import login_required, login_user, logout_user
from flask_restful import Resource
from api.models.users import Users


class LoginResource(Resource):
    """
    Controls the login operations
    """
    def post(self):

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


class DeleteResource(Resource):
    """
    Controls the delete operations
    """
    @login_required
    def delete(self):
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
