from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

server = Flask(__name__)
CORS(server)

@server.route('/', methods=['GET', 'POST'])
def login():
    return render_template('home.html') 

@server.route('/create', methods=['GET', 'POST'])
def create_message():
    return render_template('create.html')

@server.route('/decode', methods=['GET', 'POST'])
def decode_message():
    return render_template('decode.html')

if __name__ == '__main__':
    server.run(debug=True)