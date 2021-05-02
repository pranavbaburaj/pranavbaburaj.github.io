import dotenv
import os
import requests

from flask import (Flask, views, jsonify, request, abort)
from flask_cors import CORS as cors
"""
Load all the environment variabled
from the .env file. The env file
contains the username and the password
"""
dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")
USERNAME = "pranavbaburaj"

app = Flask(__name__)
cors(app)

class ArrangeProjects(object):
    limit = 3

    def __init__(self, project_list):
        self.project_list = project_list
        self.top_indexes = self.find_top_stars(self.project_list)

        self.projects = []

    def find_top_stars(self, projects):
        """
        Get the number of stars in each and every project
        and sort it as ana array and returns the reversed
        array

        Args:
            projects ([dict]): A dict containing the number of stars
            and the array of projects with the corresponding number of stars

        Returns:
            list: The stars gained by the projects sorted in 
            descending order
        """
        data = sorted([int(key) for key in projects.keys()])
        return data[::-1]

    def find_top_projects(self):
        """
        Return the top three projects based 
        on the number of stars

        Returns:
            list: The list of top projects
        """
        for index in range(len(self.top_indexes)):
            current_index = str(self.top_indexes[index])
            for project in self.project_list.get(current_index):
                if len(self.projects) >= 3:
                    break

                self.projects.append(project)

        return self.projects


class GithubResponse(object):
    headers = {"Accept": "application/vnd.github.mercy-preview+json"}
    required_fields = [
        "name", "html_url", "description", "homepage", "stargazers_count"
    ]

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def create_request(self):
        repos = ArrangeProjects(
            self.remove_unwanted_fields(
                requests.get(self.get_api_url(self.username),
                             headers=self.headers,
                             auth=(self.username, self.api_key)).json(),
                self.required_fields)).find_top_projects()

        return repos

    def remove_unwanted_fields(self, repos, fields):
        projects = []
        for repo in repos:
            project = {}
            for dict_key in fields:
                project[dict_key] = repo.get(dict_key)
            projects.append(project)

        return self.assign_indexes(projects)

    def assign_indexes(self, data):
        return_value = {}
        for index, element in enumerate(data):
            stars = element["stargazers_count"]
            if not return_value.get(str(stars)):
                return_value[str(stars)] = []
            return_value[str(stars)].append(element)
        return return_value

    def get_api_url(self, username):
        return f"https://api.github.com/users/{self.username}/repos"


class IndexView(views.MethodView):
    def post(self):
        return jsonify(status=404, message="post not supported")

    def get(self):
        response = GithubResponse(USERNAME, TOKEN).create_request()
        return jsonify({"data": response})


app.add_url_rule("/", view_func=IndexView.as_view("index"))
app.run(debug=True)
