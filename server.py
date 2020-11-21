from flask import Flask, send_from_directory, make_response, abort, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__,static_folder='client/public',static_url_path='')

@app.route('/api/', methods=['GET'])
@cross_origin()
def Welcome():
    return make_response({"message": "Welcome to the API!!!"}, 200)
    




@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/images/<path:path>", methods=['GET'])
def images(path):
    return send_from_directory('images', path)

@app.route("/<path:path>", methods=['GET'])
def home(path):
    return send_from_directory('../client/public', path)




@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Server Error: Unable to process request.'}), 500)


if __name__ == '__main__':
    app.run(port=3000)