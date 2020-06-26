# BattleSauder
[BattleSnake](https://play.battlesnake.com/) implementation.

Note that code changes BattleSnake's x-y coordinates to graphics coordinates.

## Requirements

Meant to be run on heroku. Recommended to have heroku and git installed and set up.

requirements.txt has additional modules that enable integration with Heroku Redis and PostgreSQL,
alongside quality of life dev tools like mypy and pytest.

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

After the script has run, you should now be within virtual environment. Then go to project directory, and enter:

```bash
pip install -r requirements.txt
flask run
```

Head to http://120.0.0.1:5000/ with command line running to see JSON response - success!

If you wish to run this local version on Heroku, simply follow steps in Start.