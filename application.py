from flask import Flask, render_template, jsonify, request
from generator import TweetGenerator

application = Flask(__name__)

markov_chain = TweetGenerator()


@application.route('/')
def home():
    markov_chain.load_generator("static/misc/markov_chain")
    return render_template('home.html')


@application.route('/tweet', methods=['GET'])
def generate():
    tweet = markov_chain.generate_tweet()
    return render_template('tweet.html', tweet=tweet)


if __name__ == "__main__":
    application.debug = True
    application.run(debug=True)
