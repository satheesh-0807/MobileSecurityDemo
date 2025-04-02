from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    response = make_response(jsonify({"message": "Hello from the Flask server!"}), 200)
    response.headers['X-Flag'] = 'CTF{Accessing_the_Flask_server_is_easy_if_you_know_how}'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
