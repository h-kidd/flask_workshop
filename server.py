from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

server = Flask(__name__)
CORS(server)

@server.route('/')
def welcome():
    return render_template('home.html') 

if __name__ == '__main__':
    server.run(debug=True)