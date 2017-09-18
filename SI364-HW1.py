## HW 1
## SI 364 F17
## Due: September 19, 2017
## 500 points

## PART 1 - 100 points

## First, set up a new-to-this-assignment conda environment. To the Canvas assignment, you should submit:
# - A screenshot showing your environment activated and deactivated. You should feel comfortable activating and deactivating a virtual environment. ## NOTE: (You can call the env whatever you want, but remember you'll have to type it a lot and we will have to see it. It's not like a password -- consider it public.)
# - A screenshot showing the result of typing conda list at the prompt when the environment is activated. 

######

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"
from flask import request
import itunespy
#import urllib2


from flask import Flask, url_for
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello'

@app.route('/class')
def welcome():
    return 'Welcome to SI 364!'



@app.route('/movie/<name>')
def movietest(name):

	try:
		moviesearch = (itunespy.search_movie(name))
		r = 0
		x = []
		for m in moviesearch:
			x.append(m)
			r += 1

		if r < 1:
			return ('Result Count: ' + '\n' + '0' + '\n\n' + 'Results: ' + '\n\n' + '[]')
			exit()


		return ('Result Count: ' + '\n' + str(r) + '\n\n' + 'Results: ' + '\n\n' + str(x))

	except:
		#x = []
		return ('Result Count: ' + '\n' + '0' + '\n\n' + 'Results: ' + '\n\n' + '[]')





if __name__ == '__main__':
    #app.run(host='localhost:5000')
    app.run(
    	host=app.config.get("HOST", "localhost"),
    	port=app.config.get("PORT", 5000)
	)    

#with app.test_request_context():


## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should seesomething like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!
