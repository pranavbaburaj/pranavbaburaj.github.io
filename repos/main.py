import dotenv
import os

from flask import Flask, views, jsonify, request, abort

"""
Load all the environment variabled
from the .env file. The env file
contains the username and the password
"""
dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

app = Flask(__name__)

class IndexView(views.MethodView):
    def get(self):
        return jsonify(status=404, message="GET not supported")

    def post(self):
        data = request.get_json(force=True).get('api_key')
        if not data:
            return abort(404, description="Resource not found")
        return "Yeah"

app.add_url_rule("/", view_func=IndexView.as_view("index"))
app.run(debug=True)

