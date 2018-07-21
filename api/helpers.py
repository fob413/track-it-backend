from os import environ
from functools import wraps
from flask import jsonify, request, make_response, g
from api.models import Users
import jwt
from api.core.flask_mail_service import FlaskMailService

# authorization decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check that the Authorization header is set
        authorization_token = request.headers.get('auth_token')
        if not authorization_token:
            response = jsonify({
                "status": "fail",
                "message": "User is not authenticated"
            })
            response.status_code = 400
            return response

        try:
          payload = jwt.decode(
            authorization_token,
            'secret',
            options={
              'verify_signature': True,
              'verify_exp': True
            }
          )
        except ValueError:
          response = jsonify({
            "status": "fail",
            "message": "User is not authenticated"
          })
          response.status_code = 401
          return response
        except jwt.ExpiredSignatureError:
            response = jsonify({
              "status": "fail",
              "message": "Authorizaition failed. Expired token."
            })
            response.status_code = 401
            return response
        except jwt.InvalidAlgorithmError as error:
            if str(error) == 'Algorithm not supported':
                response = jsonify({
                  "status": "fail",
                  "message": "Encoding algorithm is invalid"
                })
                response.status_code = 500
                return response
            else:
                response = jsonify({
                  "status": "fail",
                  "message": "User is not authenticated"
                })
                response.status_code = 401
                return response
        except jwt.DecodeError as error:
            if str(error) == 'Signature verification failed':
                response = jsonify({
                  "status": "fail",
                  "message": "An error occured while decoding"
                })
                response.status_code = 401
                return response
            else:
                response = jsonify({
                  "status": "fail",
                  "message": "token provided is invalid"
                })
                response.status_code = 401
                return response
        
            # now return wrapped function
        current_user = CurrentUser(
          payload['sub']
        )

        # set current user in flask global variable, g
        g.current_user = current_user
        return f(*args, **kwargs)
    return decorated


class CurrentUser(object):
    def __init__(self, id):
        self.user_id = id

    def __repr__(self):
        return ("<CurrentUser \n"
                "user_id - {} \n"
                ).format(self.user_id)


def validate_type(item, input_type):
    return type(item) is input_type


def validate_request(*expected_args):
    """ This method validates the Request payload.
    Args
        expected_args(tuple): where i = 0 is type and i > 0 is argument to be
                            validated
    Returns
      f(*args, **kwargs)
    """

    def real_validate_request(f):
        type_map = {"str": "string",
                    "list": "list",
                    "dict": "dictionary",
                    "int": "integer"}
        @wraps(f)
        def decorated(*args, **kwargs):
            if not request.json:
                responseObject= {
                        "status": "fail",
                        "message": "Request must be a valid JSON"
                    }
                return make_response(jsonify(responseObject)), 400
            payload = request.get_json()
            if payload:
                for values in expected_args:
                    for value in values:
                        if value == values[0]:
                            continue
                        if value not in payload or ((
                                values[0] != dict and not payload[value])):
                            responseObject= {
                                "status": "fail",
                                "message": value + " is required"
                            }
                            return make_response(jsonify(responseObject)), 400
                        elif not validate_type(payload[value], values[0]):
                            responseObject = {
                                "status": "fail",
                                "message": value + " must be a valid " +
                                         type_map[ values[0].__name__]
                                }
                            return make_response(jsonify(responseObject)), 400
            return f(*args, **kwargs)
        return decorated
    return real_validate_request

class NotificationRecipient:
    def __init__(self):
        pass

    def user_recipient(*args):
        print(args)
        email = {
            'config':app,
            'subj': subject,
            'from': SENDER,
            'to': user_email,
            'body': body
        }
        return FlaskMailService.send_mail(email)
