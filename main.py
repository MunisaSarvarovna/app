from app import FrameWorkApp
import json


app = FrameWorkApp()


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)

    return users


def load_view():
    with open("view.json", "r") as file:
        data = json.load(file)

    return data

def load_about():
    with open("about.json", "r") as file:
        about = json.load(file)

    return about




cnt = load_view()


@app.route("/home")
def home(request, response):
    global cnt
    cnt += 1
    with open("view.json", "w") as file:
        json.dump(cnt, file)
    response.text = f"Home pagedan uyquli salom! - {cnt}"


cn = load_about()

@app.route("/about")
def about(request, response):
    global cnt
    cnt += 1
    with open("about.json","w") as file:
        json.dump(cnt,file)
    response.text = f"About pagedan Shabnamga salom! - {cnt}"



@app.route("/u/{id}")
def get_info(request, response, id):
    users = load_users()
    user = users.get(id, "Bunday user yo'q!")

    response.text = json.dumps(user)


"""
    "/home" : home,
    "/about" : about,
    "/sardor" : sardor,
    "/u/munisa" : user,
    "/u/zoir" : user
"""

"""
    "/u/id" => "/u/1"

"""