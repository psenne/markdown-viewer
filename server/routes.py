from app import api, app, db
from server.models import Document, document_schema, documents_schema
from flask import send_from_directory, make_response, abort, request, jsonify
from flask_restful import Resource
from flask_cors import CORS, cross_origin


class Home(Resource):
    def get(self):
        return send_from_directory(app.static_folder, 'index.html')


class StaticFiles(Resource):
    def get(self, contents):
        return send_from_directory(app.static_folder, contents)


class HandleDocument(Resource):
    def get(self, doc_id):
        document = Document.query.filter_by(uuid=doc_id).first_or_404()
        return document_schema.dump(document)

    def post(self, doc_id):
        new_doc = Document(uuid=doc_id, userId=1)
        db.session.add(new_doc)
        db.session.commit()
        return document_schema.dump(new_doc)

    def patch(self, doc_id):
        document = Document.query.filter_by(uuid=doc_id).first_or_404()
        if request.json['text']:
            document.text = request.json['text']

        db.session.commit()
        return document_schema.dump(document)

class HandleDocuments(Resource):
    def get(self):
        documents = Document.query.all()
        return documents_schema.dump(documents)



api.add_resource(HandleDocuments, '/api/documents')
api.add_resource(HandleDocument, '/api/document/<doc_id>')
api.add_resource(StaticFiles, '/<path:path>')
api.add_resource(Home, '/')
