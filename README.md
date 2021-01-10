<br />
<p align="center">

  <h3 align="center">NBAPI - Free NBA Live Score API</h3>

  <p align="center">
    Get all of the live scores of today's NBA games for FREE!
  </p>
</p>

<!-- ABOUT THE PROJECT -->

## About The Project

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:

- Your time should be focused on creating something amazing. A project that solves a problem and helps others
- You shouldn't be doing the same tasks over and over like creating a README from scratch
- You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have have contributed to expanding this template!

A list of commonly used resources that I find helpful are listed in the acknowledgements.

## Usage

The API can handle several query types: you can either get all the live games for the day or the game that is being played by a specific team for that day.

- Get all the games being played today
  ```sh
  https://nbscrape.herokuapp.com/?team=all
  ```
- Get the live stats on the Charlotte Hornets game (if they're playing today)
  ```sh
  https://nbscrape.herokuapp.com/?team=cha
  ```

These will return team1, team2, team1's score, team2's score, and the time left in the game in the form of an object that you can access contents of via variable "team1", "team2", "team1_score", "team2_score", and "timeLeft". If timeLeft is "FINAL", the game is over. If the game has not yet started but will start later in the day, timeLeft will provide the starting time of the game.

### Common Errors

1. Invalid Team name

Make sure to only use the following team names to avoid this error: "ATL","BKN","BOS","CHA","CHI","CLE","DAL","DEN","DET","GSW","HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","NYK","OKC","ORL","PHI","PHX","POR","SAC","SAS","TOR","UTA","WAS" or "all" for all teams.

2. Please use team query to query scores

This means most likely that you didn't give a team query to the server. Please make sure to use the template of "https://nbscrape.herokuapp.com/?team=***" to get a team's score.

3. Too many requests - try again later

Please do not spam the server with requests every second. The server will be able to handle your requests every 5-10 seconds. Please consider this when using this API.

4. \*\*\* is not playing today

Simply means the team you are looking for isn't playing. You probably want to handle this on your side or look for a team that is.

### Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [r/NBA](https://www.reddit.com/r/nba)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

<!-- GETTING STARTED -->

## Getting Started

Get a local copy of the code up and running by following these steps:

### Prerequisites

Make sure you have pip and python3 installed

- pip
  ```sh
  sudo apt install python3-pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nicholaswang2000/NBAScraper
   ```
2. Install pip packages
   ```sh
   pip install
   ```
3. Run, test, etc using
   ```sh
   flask run
   ```
