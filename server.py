import requests
import bs4

from flask import Flask, render_template
app = Flask(__name__)

REDDIT = 'http://www.reddit.com/r/soccer/'
WAITTIME = '.........................................'

@app.route('/')
def hello():
	print "hello"
	request = requests.get(REDDIT, headers={"User-Agent":"reddit-reader/1.0 by jfayd"})
	html = request.text
	soup = bs4.BeautifulSoup(html)
	adivs = soup.find_all('a', attrs = { 'class' : 'title may-blank '  })
	titles = [a.contents for a in adivs]
	return render_template('index.html', reddits=titles, texties=titles)
	
	print "made it"
	# return "HEllo WOrld"

if __name__ == "__main__":
	print "up and running"
	app.debug = True
	app.run()


# Skips over non-Unicode entries
# Overlapped lines

# Stops reading after first, even though all print
# refresh causes "run loop already started"

