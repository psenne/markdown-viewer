from app import api, app
from server.documents import Documents
from flask import send_from_directory, make_response, abort, request, jsonify
from flask_restful import Resource
from flask_cors import CORS, cross_origin


class GetDocuments(Resource):
    def get(self):
        documents = Documents.query.all()
        return [Documents.serialize(document) for document in documents]


api.add_resource(GetDocuments, '/api/documents')


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/images/<path:path>", methods=['GET'])
def images(path):
    return send_from_directory('images', path)


@app.route("/<path:path>", methods=['GET'])
def home(path):
    return send_from_directory('../client/public', path)


# @app.route('/api/', methods=['GET'])
# @cross_origin()
# def Welcome():
#     return make_response({"message": "Welcome to the API!!!"}, 200)

# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': str(error)}), 404)

# @app.errorhandler(500)
# def not_found(error):
#     return make_response(jsonify({'error': 'Server Error: Unable to process request.'}), 500)
