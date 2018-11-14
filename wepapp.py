from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

with open('county_demographic.json') as demographics_data:
        counties = json.load(demographics_data)

def toOption(s):
    return "<option value=" + s + " >" + s + "</option>"
        
def get_states_opions():
    listOfStates = []
    print(type(listOfStates))
    for c in counties:
        if c["State"] not in listOfStates:
            listOfStates.append(c["State"])
    print(listOfStates)
    return listOfStates 
        
@app.route("/")
def render_creed():
    str = ""
    for cc in get_states_opions():
        str += toOption(cc)
        
    
    print(str)
    return render_template('bam.html', strr = Markup(str))

def pop(states):
    states = population["2014 Population"]
    for pop in states:
        if pop["population2014"] > first:
            first = states["population"]
    return first
    
    if __name__=="__main__":
    app.run(debug=True, port=54321)