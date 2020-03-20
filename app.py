from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from num2words import num2words as n2w

app = Flask(__name__)
api = Api(app)


class Num2WordAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('type', type=str, required=True)
        self.reqparse.add_argument('language', type=str, required=True)
        self.reqparse.add_argument('number', type=float, required=True)
        super(Num2WordAPI, self).__init__()

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response('<!doctype html><title>Num2Word - API</title><h1>Num2Word API</h1>', 200, headers)

    def post(self):
        data = self.reqparse.parse_args()

        if data['type'] == "":
            data['type'] = 'cardinal'

        if data['language'] == "":
            return {
                'language': 'No language selected!',
                'message': 'Nothing converted!',
                'status': 'ERROR'
                }
        if data['number'] == "":
            return {
                'language': data['language'],
                'message': 'No number!',
                'status': 'ERROR'
                }
        if data['type'] == 'currency' and data['language'] == 'pl':
            converted = n2w(data['number'], lang=data['language'], to=data['type'], currency='PLN')
            return {
                'language': data['language'],
                'message': converted,
                'status': 'OK'
            }
        elif data:
            converted = n2w(data['number'], lang=data['language'], to=data['type'])
            return {
                'language': data['language'],
                'message': converted,
                'status': 'OK'
            }
        else:
            return {
                'language': 'Something when wrong!',
                'message': 'Something when wrong!',
                'status': 'ERROR'
            }


class HelloWorld(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response('<!doctype html><title>Num2Word - Framework</title><h1>Num2Word Framework</h1>', 200, headers)


api.add_resource(HelloWorld, '/')
api.add_resource(Num2WordAPI, '/api')
