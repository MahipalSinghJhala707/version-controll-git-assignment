from flask import Flask , request, render_template
from dotenv import load_dotenv
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi("1"))
db = client.users
collection = db["items"]



app = Flask(__name__)


@app.route('/submittodoitem', methods=['POST'])
def submit():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")
    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return "Item Stored Successfully"

@app.route('/')
def todo():
    return render_template('index.html')
    


if __name__ == "__main__":
    app.run(debug=True)
