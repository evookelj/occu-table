#!/usr/bin/python
import csv
from random import uniform

occs = {}
newDict = {}

def readToDict():
    with open('data/occUpdate.csv') as csvfile:
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
