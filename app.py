from flask import Flask, render_template
from utils import occupation

app = Flask(__name__)

@app.route("/")
def root():
    return "Hola"

@app.route("/occupation")
def renderOccupation():
    randomOcc = occupation.getRandOccupation()
    return render_template('main.html', title="Occupations", link=occupation.occs[randomOcc][1], job = randomOcc, table=occupation.newDict)

if __name__ == "__main__":
    app.debug = True
    app.run()
