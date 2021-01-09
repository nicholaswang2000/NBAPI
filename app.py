import flask
from flask import request
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from bracket import Game

app = flask.Flask(__name__)
teams = ["all","atl","bkn","bos","cha","chi","cle","dal","den","det","gsw","hou","ind","lac","lal","mem","mia","mil","min","nop","nyk","okc","orl","phi","phx","por","sac","sas","tor","uta","was"]

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
        return "Too many requests - try again later (every 5-10 seconds)"
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
            if team == team1.lower() or team == team2.lower():
                return game_json
            titles.append(game_json)
    if team == "all":
        titles_json = json.dumps(titles)
        return titles_json
    else:
        return team + ' is not playing today. Please enter another team or check back tomorrow.'