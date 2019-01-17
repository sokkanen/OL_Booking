from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Erkki Esimerkki"

lista = [1,1,2,3,5,8,11]

esineet = []
esineet.append(Item("eka"))
esineet.append(Item("toka"))
esineet.append(Item("kolmas"))
esineet.append(Item("neljäs"))


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

if __name__ == "__main__":
    app.run(debug=True)