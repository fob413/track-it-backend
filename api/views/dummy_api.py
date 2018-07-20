from flask import request, jsonify
from flask_restful import Resource


class Dummy(Resource):

    def get(self):
        response = dict(
            status='success',
            message='Welcome to Track It Api'
        )
        return jsonify(response)