from http.client import responses

from app import FrameWorkApp
import json

app = FrameWorkApp()

def load_users():
    with open("users.json","r") as file:
        users = json.load(file)

    return users

@app.route("/")
def main(request, response):
    response.text = "siz glavniy ekrandasiz"

@app.route("/home")
def home(request,response):
    response.text ="home pagedan uyquli salom"

@app.route("/about")
def about(request,response):
    response.text ="about pagega salom"

@app.route("/u/id")
def get_info(requests,response,id):
    users = load_users()
    user = users.get(id,"bunday yoq")

    response.text = json.dumps(user)

@app.route("/admin/{id}")
def get_info(requests,response,id):
    admins = load_users()
    admin = admins.get(id,"bunday yoq")

    response.text = json.dumps(admin)





