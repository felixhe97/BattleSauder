# BattleSauder
Communitech BattleSnake implementation

## Requirements

Meant to be run on heroku. Recommended to have heroku and git installed and set up.

## Start

Clone this repository, then go to cloned directory.

On command line while within cloned directory:

```bash
heroku create
git push heroku master
heroku config:set WEB_CONCURRENCY=3
heroku open
```

A browser page should be opened with JSON response - success!

## Run Locally

Clone this repository, then go to cloned directoy.

On command line while within cloned directory:

```bash
python -m venv .
cd Scripts
```

Then depending on OS, run relevant 'activate' script to get into virtual environment.

```bash
cd ..
pip install -r requirements.txt
flask run
```

Head to http://120.0.0.1:5000/ with command line running to see JSON response - success!