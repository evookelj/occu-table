#!/usr/bin/python

from random import uniform
from flask import Flask, render_template
import csv

occs = {}
newDict = {}
app = Flask(__name__)

def readToDict():
    import csv
    with open('occUpdate.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row['Job Class']
            percent = float(row['Percentage'])
            link = row['Link']
            if (job != 'Total'): occs[job] = [percent, link]

def pickWeighted():
    for occ in occs:
        newDict[occ] = occs[occ][0]
    rand = uniform(0, sum(newDict.itervalues())) #rand float from 0 to sum of vals
    sigma = 0.0
    for key, weight in newDict.iteritems():
        sigma += weight
        if rand < sigma: return key;
    return key

def getRandOccupation():
    readToDict()
    return pickWeighted()

@app.route("/")
def homePage():
    randomOcc = getRandOccupation()
    return render_template('main.html', title="Occupations", link=occs[randomOcc][1], job = randomOcc, table=newDict)

if __name__ == "__main__":
    app.debug = True
    app.run()
