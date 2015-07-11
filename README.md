# reddit-reader

Reddit Reader: ingest reddit audibly.

* Python - Flask
* Javascript - ResponsiveVoice.js, jQuery
* HTML/CSS

## Visit redditreader.herokuapp.com
Bookmark it and let it become part of your commute.

## Upcoming TODO
Currently monitors reddit.com/r/soccer.
* Support other subreddits, multireddits, user-inputted, user-logins
* Save feature to bookmark interesting titles for later
* Voice support so control app without hands or visual need

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py migrate
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```


