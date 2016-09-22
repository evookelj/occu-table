#!/usr/bin/python

from random import uniform
from flask import Flask, render_template
import csv

occs = {}
app = Flask(__name__)

def readToDict():
    import csv
    with open('occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row['Job Class']
            percent = float(row['Percentage'])
            if (job != 'Total'): occs[job] = percent

def pickWeighted():
    rand = uniform(0, sum(occs.itervalues())) #rand float from 0 to sum of vals
    sigma = 0.0
    for key, weight in occs.iteritems():
        sigma += weight
        if rand < sigma: return key;
    return key

def getRandOccupation():
    readToDict()
    return pickWeighted()

@app.route("/")
def homePage():
    randomOcc = getRandOccupation()
    return render_template('main.html', title="Occupations", job = randomOcc, table=occs)

if __name__ == "__main__":
    app.debug = True
    app.run()
