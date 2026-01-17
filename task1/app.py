from flask import Flask 

import json


app = Flask(__name__)



@app.route('/api')
def get_data():
    with open('data.json' , 'r') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    app.run(debug=True)


