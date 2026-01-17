from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi("1"))
db = client.users
collection = db["email_pass"]

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        try:
            form_data = dict(request.form)

            if not form_data:
                raise ValueError("Form data is empty")

            client.admin.command("ping")

            collection.insert_one(form_data)

            return redirect(url_for("success"))

        except Exception as e:
            error = str(e)

    return render_template("index.html", error=error)


@app.route("/submit")
def success():
    return "Data submitted successfully"


if __name__ == "__main__":
    app.run(debug=True)
