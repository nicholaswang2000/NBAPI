import flask
from flask import request
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from bracket import Game

app = flask.Flask(__name__)
teams = ["atl","bkn","bos","cha","chi","cle","dal","den","det","gsw","hou","ind","lac","lal","mem","mia","mil","min","nop","nyk","okc","orl","phi","phx","por","sac","sas","tor","uta","was"]

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/', methods=['GET'])
def home():

    team = ""
    try:
        team = request.args['team']
    except:
        return 'Please use team query to query scores'
        
    team = team.lower()
    if team not in teams:
        return 'Invalid Team name.'+'Valid team names are:\n'+'"ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS"\n'+'Or "all" to get all of today\'s games.'

    try:
        my_url = "https://old.reddit.com/r/nba/"
        uClient = urlopen(my_url)
        page_html = uClient.read()
        uClient.close()
    except:
        users_ref = db.collection('teams')
        docs = users_ref.stream()

        teamData = {}
        for doc in docs:
            if team.lower() == doc.id:
                teamData = doc.to_dict()
                break

        game = Game(team.upper(), teamData['opponent'].upper(), teamData['homeScore'], teamData['oppScore'], teamData['timeLeft'])
        game_json = json.dumps(game.__dict__)
        return game_json

    page_soup = soup(page_html, "html.parser")
    titlebox_soup = page_soup.find("div",{"class":"usertext-body may-blank-within md-container"})
    titlebox = titlebox_soup.find("div", { "class" : "md" }).blockquote.ul

    titles = []
    for li in titlebox:
        if li != "\n" and li.strong:
            title = li
            table = title.findAll('strong')
            if title.find('a'):
                team1 = table[0].next_element
                team2 = table[1].next_element
                team1_score = title.next_element.next_element.findNextSibling(text=True)
                team2_score = title.next_element.next_element.next_element.next_element.findNextSibling(text=True)
                timeLeft = title.find('a').next_element
            else:
                team1 = table[0].next_element
                team2 = table[1].next_element
                team1_score = "N/A"
                team2_score = "N/A"
                timeLeft = title.next_element.next_element.next_element.next_element.findNextSibling(text=True)
            game = Game(team1, team2, team1_score, team2_score, timeLeft)
            game_json = json.dumps(game.__dict__)

            if team == team1.lower():
                updateFirestore(team, True, team1_score, team2_score, team2, timeLeft)
                return game_json
            elif team == team2.lower():
                updateFirestore(team, True, team2_score, team1_score, team1, timeLeft)
                return game_json

            titles.append(game_json)
    updateFirestore(team, False, "-", "-", "-", "-")

    game = Game(team, "-", "-", "-", "-")
    game_json = json.dumps(game.__dict__)
    return game_json


def updateFirestore(team, playing, homeScore, oppScore, opponent, timeLeft):
    doc_ref = db.collection('teams').document(team)
    doc_ref.set({
        'homeScore': homeScore,
        'oppScore': oppScore,
        'opponent': opponent,
        'playing': playing,
        'timeLeft': timeLeft
    })


@app.route('/all', methods=['GET'])
def all():
    print("Hi")
    return "Hi"