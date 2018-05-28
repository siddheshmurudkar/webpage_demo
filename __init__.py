from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template, g
import json
import os
import requests
import random
import string

app = Flask(__name__)

dome1 = []
dome2 = []
dome3 = []
dome4 = []


@app.route('/shopping')
def list():
    return render_template('shopping.html', dome1=dome1, dome1Len=len(dome1), dome2=dome2, dome2Len=len(dome2), dome3=dome3, dome3Len=len(dome3), dome4=dome4, dome4Len=len(dome4))

@app.route('/layout')
def layout():
    return render_template('layout.html', domeA1=a1, domeA2=a2, domeA3=a3, domeA4=a4,dome1=dome1)

@app.route('/live')
def status():
    return render_template('responsive.html', dome1=dome1, dome1Len=len(dome1), dome2=dome2, dome2Len=len(dome2), dome3=dome3, dome3Len=len(dome3), dome4=dome4, dome4Len=len(dome4))


@app.route('/demo')
def live():
    return render_template('live.html', dome1=dome1, dome1Len=len(dome1), dome2=dome2, dome2Len=len(dome2), dome3=dome3, dome3Len=len(dome3), dome4=dome4, dome4Len=len(dome4))

@app.route('/<device_id>/<person_id>')
def trackPerson(device_id, person_id):
    g.device_id = device_id
    g.person_id = person_id
    #person_name = os.environ.get(g.person_id)
    if g.device_id == "beacon1":
        dome1.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)

    if g.device_id == "beacon2":
        dome2.append(g.person_id)
        if g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
    if g.device_id == "beacon3":
        dome3.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
        elif g.person_id in dome4:
            dome4.remove(g.person_id)
    if g.device_id == "beacon4":
        dome4.append(g.person_id)
        if g.person_id in dome2:
            dome2.remove(g.person_id)
        elif g.person_id in dome3:
            dome3.remove(g.person_id)
        elif g.person_id in dome1:
            dome1.remove(g.person_id)
        len1 = len(dome1)
        if len1 == 0:
            a1 = ""
            a2 = ""
            a3 = ""
            a4 = ""
        if len1 == 1:
            a1 = dome1[0]
        if len1 == 2:
            a1 = dome1[0]
            a2 = dome1[1]
        if len1 == 3:
            a1 = dome1[0]
            a2 = dome1[1]
            a3 = dome1[2]
        if len1 == 4:
            a1 = dome1[0]
            a2 = dome1[1]
            a3 = dome1[2]
            a4 = dome1[3]
    return "<h3> OK </h3>"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def page():
   return "<h1> hi there, whatsup!!</h1>"
if __name__ == "__main__":
   app.run()
