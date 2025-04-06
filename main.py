from http.client import responses

from app import FrameWorkApp

app = FrameWorkApp()

@app.route("/")
def main(request, response):
    response.text = "siz glavniy ekrandasiz"



@app.route("/home")
def home(request,response):
    response.text ="home pagedan uyquli salom"



@app.route("/about")
def about(request,response):
    response.text ="about pagega salom"


@app.route("/sardor")
def sardor(request,response):
    response.text ="sardordan salom"


@app.route("/shabnam")
def shabnam(request,response):
    response.text =("ismi:Shabnam,"
                    "yoshi:16,"
                    "hobby:rasm chizsh,"
                    "yoqtirgan rang:sariq,qora,"
                    "yoqtrgan oqat:kfs,")



#glavnida glavni ekran i bita orto haqida malumot

