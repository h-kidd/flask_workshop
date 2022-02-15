from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(server)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bob'}
    return render_template('index.html', title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True)